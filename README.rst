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
Copy the turorial directory in your home directory.
Open a terminal and change in libreoffice directory:
::

    cd .config/libreoffice/4/user/Scripts/python

If the directory Scripts/python doesnot exists create it:
::

    mkdir -p .config/libreoffice/4/user/Scripts/python

Create a soft link to the tutorial\'s file:
::

    ln -s /home/user/lo_python_tutorial/report

Open a LibreOffice Writer document and go to **Tools --> Macros --> Run Macro --> My Macros --> report --> homelibrar_sqlite --> list_books** and click execute.

Windows
*******
Under work.

Links
#####
* `Python <https://www.python.org/>`_
* `LibreOffice <https://www.documentfoundation.org/>`_
* `LibreOffice API <https://api.libreoffice.org/>`_
