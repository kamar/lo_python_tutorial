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
Under work.

Links
#####
* `Python <https://www.python.org/>`_
* `LibreOffice <https://www.documentfoundation.org/>`_
* `LibreOffice API <https://api.libreoffice.org/>`_
* `Interface-oriented programming in OpenOffice / LibreOffice <http://christopher5106.github.io/office/2015/12/06/openoffice-libreoffice-automate-your-office-tasks-with-python-macros.html>`_
