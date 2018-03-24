#!/usr/bin/env python3
import os
import sqlite3
import datetime
import uno

from com.sun.star.text.ControlCharacter import PARAGRAPH_BREAK
from com.sun.star.style.ParagraphAdjust import RIGHT


def login(dbname):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()

    return conn, curs


def list_books(*args):

    ctx = uno.getComponentContext()
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)

    # open a writer document
    doc = desktop.loadComponentFromURL("private:factory/swriter", "default", 0, ())

    pageStyle = doc.getStyleFamilies().getByName("PageStyles")
    defProp = pageStyle.getByName("Standard")

    defProp.setPropertyValue("IsLandscape", True)
    defProp.setPropertyValue("Width", 29700)
    defProp.setPropertyValue("Height", 21000)

    text = doc.Text
    cursor = text.createTextCursor()
    cursor.ParaStyleName = "Heading 1"
    text.insertString(cursor, "Κατάσταση Βιβλίων", 0)
    text.insertControlCharacter(cursor, PARAGRAPH_BREAK, 0)
    cursor.ParaStyleName = "Standard"

    # Change your path to the database.
    con, cur = login('/home/km/.config/libreoffice/4/user/Scripts/python/homelibrary.db')

    qry = "select b.isbn, b.title, a.firstname || ' ' || a.surname as author, b.copies_standard, b.copies_avail from tbl_books b, tbl_author a where b.author_id=a.author_id order by b.author_id;"
    cur.execute(qry)
    result = cur.fetchall()
    con.close()

    result.insert(0, ("ISBN", "ΤΙΤΛΟΣ", "ΣΥΓΓΡΑΦΕΑΣ", "ΣΥΝΟΛΟ", "ΑΠΟΘΕΜΑ"))
    result_len = len(result)

    table_01 = doc.createInstance("com.sun.star.text.TextTable")
    table_01.initialize(result_len, len(result[0]))
    table_01.setName("TableBooks")
    text.insertTextContent(cursor, table_01, 0)

    tblColSeps = table_01.TableColumnSeparators

    tblColSeps[0].Position = 1400
    tblColSeps[1].Position = 5500
    tblColSeps[2].Position = 8000
    tblColSeps[3].Position = 9000

    table_01.TableColumnSeparators = tblColSeps

    table_01.setPropertyValue("HeaderRowCount", 1)
    table_01.setPropertyValue("RepeatHeadline", True)
    table_01.setPropertyValue("BackTransparent", uno.Bool(0))
    table_01.setPropertyValue("BackColor", 13421823)

    table_01.setDataArray(result)
    rows_01 = table_01.Rows
    row_01 = rows_01.getByIndex(0)
    row_01.setPropertyValue("BackTransparent", uno.Bool(0))
    # row_01.setPropertyValue("BackColor", 6710932)
    # table_01.Rows.insertByIndex(len(result), 1)
    oRange = table_01.getCellRangeByName("A2:E{0}".format(result_len))
    oRange.CharHeight = 9.5

    oRange = table_01.getCellRangeByName("D2:E{0}".format(result_len))
    oRange.ParaAdjust = RIGHT

    standard_style = doc.StyleFamilies.getByName("PageStyles").getByName("Standard")

    standard_style.setPropertyValue("FooterIsOn", True)
    f_text = standard_style.getPropertyValue("FooterText")
    f_cursor = f_text.createTextCursor()
    f_cursor.setPropertyValue("CharHeight", 8)
    f_text.insertString(f_cursor, "Προγραμματισμός: Κώνστας Μαρματάκης", 0)
    f_text.insertControlCharacter(f_cursor, PARAGRAPH_BREAK, 0)
    d = datetime.date.today()
    f_text.insertString(f_cursor, d.strftime("%d-%m-%Y"), 0)
    f_text.insertControlCharacter(f_cursor, PARAGRAPH_BREAK, 0)
    oField = doc.createInstance("com.sun.star.text.TextField.PageNumber")
    oField.NumberingType = 4  # Arabic
    f_text.insertTextContent(f_cursor, oField, 0)
    f_cursor.ParaAdjust = 1

g_exportedScripts = (list_books,)
