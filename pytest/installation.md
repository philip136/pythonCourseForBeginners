# <span style="font-family:Helvetica; font-size:2em;">Pytest</span>

## <span style="font-family:Helvetica; font-size:1em">Installation</span>
Firstly you must install a pytest module, you can install pytest via `pip`.
However first we should create an environment for collecting packages.
```commandline
python -m venv env  # after execution we'll have a new folder named `env` in the current directory
```
After that we must activate this environment.
```commandline
env/scripts/activate
```
After execution, we will see `(env)` in front of the name of the current director like that:
`(env) PS C:\Users\......`
When environment has activated, we must install pytest.
```commandline
pip install pytest
```
When you have installed all dependencies, you can perform the following command:
```commandline
python -m pip freeze > requirements.txt
```
After that, you will have a new `requirements.txt` file with a list of dependencies. The content of the file will look like this:
```commandline
toml==0.10.2
types-cryptography==3.3.23
tzdata==2021.5
tzlocal==2.1
uritemplate==3.0.1
urllib3==1.24.3
websocket-client==1.3.1
wrapt==1.14.0
xmltodict==0.12.0
yarl==1.6.3
zipp==3.7.0
```
To install all dependencies use the following command:
```commandline
python -m pip install -r requirements.txt
```


The next part [_here_](https://github.com/philip136/pythonCourseForBeginners/blob/development/pytest/fixtures.md)