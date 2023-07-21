# Gaggle: let’s get going 
An app to help keep you and your friends connected and on the same page for your travels. 

## Server Installation Instructions
1. Fork and clone this repository to your local environment
1. Once in your code editor enter the following commands
```
$ pipenv install
$ pipenv shell
$ npm install –prefix client
```
3. Navigate to `$ cd /server`  and create a `$ touch .env` file
3. Add .env to your .gitignore and go ahead and commit that
3. Add `SECRET_KEY=` in the file, and populate that with a secure key
3. From /server enter the following commands in the terminal
```
$ export FLASK_APP=app.py
$ flask db init
$ flask db migrate
$ flask db upgrade
$ python seed.py
```
7. You’re now ready to start the server and start the client
8. from /server $ python app.py
9. from /client $ npm start


##Licensing
MIT License Copyright (c) 2023
