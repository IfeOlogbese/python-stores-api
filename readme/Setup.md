# Setup Python Application

1. Install Flask
    `pip install flask`

2. Create virual env
    - `pip install virtualenv`
    - `virtualenv venv --python=/c/Users/ologb/AppData/Local/Programs/Python/Python37/python.exe`
    *OR*
    - `virtualenv venv --python=C:/Users/ologb/AppData/Local/Programs/Python/Python37/python.exe`
    - `source venv/Scripts/activate` *or* `. venv/Scripts/activate` *or* `./venv/Scripts/activate.bat` for windows
    - `source venv/bin/activate` for mac
    - `deactivate` to deactivate venv

3. Install Flask-RESTful
    - `pip install Flask-RESTful`

# Setup Application Authentication

4. Install Flask-JWT
    - `pip install Flask-JWT`

5. Install PyLint
    - `pip install -U pylint`

6. Install Autopep8 for code formatting
    - `pip install autopep8`

7. Install MongoDb Driver for Storage
    - `pip install pymongo`
    
Useful Commands
-----------------
1. `pip freeze` returns a list of installed libraries

2. In a case where *vscode* doesn't choose the right python evironment, you should navigate to the project directory and run
    ```
    cd python-workspace
    code -n python-workspace
    code . -n
    ```
    or better still reference [https://stackoverflow.com/questions/50905636/e0401unable-to-import-flask]
