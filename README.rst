*************************************
LibreOffice Python Scripting Tutorial
*************************************

**Author:** *Konstas Marmatakis*


Description
###########

An example how to write a python script in LibreOffice writer.
No error handling included.


How to run
##########
Linux
*****
Copy the turorial directory in your home directory, or clone from the repository.
::

    git clone https://github.com/kamar/lo_python_tutorial.git

Open a terminal and change in libreoffice directory:
::

    cd .config/libreoffice/4/user/Scripts/python

If the directory Scripts/python does not exists create it:
::

    mkdir -p .config/libreoffice/4/user/Scripts/python

Create a soft link to the tutorial\'s file:
::

    ln -s /home/user/lo_python_tutorial/report

Open a LibreOffice Writer document and go to **Tools --> Macros --> Run Macro --> My Macros --> report --> homelibrary_sqlite --> list_books** and click run.

Windows
*******
Open a new terminal window and move to the LibreOffice directory:
::

    cd C:\Program Files\LibreOffice\program

Execute:
::

    python.exe --version

Find the python version from the Python site and install it.
In the homelibrary_sqlite.py script find the line:
::

    try:
        import sqlite3
    except ImportError:
        # Import error, on windows. Add the path to your python installation.
        # Here for my pc, in home directory AppData\....
        np = os.path.join(os.path.expanduser("~"), "AppData\Local\Programs\Python\Python35\Lib")
        sys.path.append(np)
        sys.path.append(os.path.join(os.path.expanduser("~"), "AppData\Local\Programs\Python\Python35\DLLs"))
        import sqlite3

and change the the paths to your python installation.

Copy the folder report to the:
::

    C:\Users\username\AppData\Roaming\LibreOffice\4\user\Scripts\python\

In the above directory open the report\homelibrary_sqlite.py and find the line: *con, cur = login(os.path.join(os.path.expanduser("~"), '.config/libreoffice/4/user/Scripts/python/homelibrary.db'))* and write your file path.

Open a LibreOffice Writer document and go to **Tools --> Macros --> Run Macro --> My Macros --> report --> homelibrary_sqlite --> list_books** and click run.

Files in tutorial
#################

#. homelibrary.db Sqlite3 sample database.
#. homelibrary_sqlite.py The script.


Links
#####
* `Python <https://www.python.org/>`_
* `LibreOffice <https://www.documentfoundation.org/>`_
* `LibreOffice API <https://api.libreoffice.org/>`_
* `Interface-oriented programming in OpenOffice / LibreOffice <http://christopher5106.github.io/office/2015/12/06/openoffice-libreoffice-automate-your-office-tasks-with-python-macros.html>`_
