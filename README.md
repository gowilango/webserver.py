## Python Web Server using Flask
## macOS
Make Sure you have NPM installed.

```
$ sudo easy_install pip
```

Install Flask
```
$ pip install flask
```

Install virtualenv (Virtual Environment Python)
```
$ sudo pip install virtualenv
```

then, Install Nose and Tornado
```
$ sudo pip install nose
```
```
$ sudo pip install tornado
```
Type 
```
$ pip list
```
to make sure flask, virtualenv, nose, tornado is installed
<br><br>

### Web Server Structure
```
main directory
|
|-- launch 
|
|-- server
    |
    |-- index.py
    |
    |-- static
    |
    |-- templates
```   
Create a virtualenv
```
$ virtualenv anyname
$ pip install flask
```

To Activate the virtualenv
```
$ cd launch
$ source bin/activate
```

To start the Python Web Server
```
$ cd server
$ python index.py runserver
```
