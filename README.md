# django-chat
A chatting app made with django-rest-framework, django-signal &amp; react.js

![chat](https://user-images.githubusercontent.com/30230336/147493438-86d86809-537b-4779-81e3-74881a54f038.gif)

# Installation Process
To install this app please follow this below steps:
### Run Backend
```
1. From the repository root, create an environment with your installed Python: `py -m venv venv`
2. Activate it on Windows: `venv\Scripts\Activate.ps1`
   - If script execution is disabled: `Set-ExecutionPolicy -Scope Process Bypass`
3. Change to the server directory: `cd server`
4. Install dependencies: `python -m pip install --upgrade pip setuptools wheel` followed by `python -m pip install -r requirements.txt`
5. Create the database: `python manage.py migrate`
6. Start the server: `python manage.py runserver`

Ubuntu activation: `source ../venv/bin/activate` after creating the environment from the repository root.
```
### Run Front-end
```
1. Change to the frontend directory: `cd client`
2. Install dependencies: `npm.cmd install`
3. Start the frontend: `npm.cmd start`
```

Now you'll be redirected to `localhost:3000` Then open two browser window and do the signup with name, email, profile image and start chatting from two different window. 
