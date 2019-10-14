# [Flask Dashboard Argon](https://appseed.us/admin-dashboards/flask-dashboard-argon)

Open-Source **admin dashboard** with **Argon** design coded in **Flask**

<br />

![Flask Dashboard Argon](https://github.com/app-generator/flask-argon-dashboard/blob/master/screenshots/flask-argon-dashboard-intro.gif)

<br />

## Build from sources

1. Clone the repo
  ```
  $ git clone https://github.com/app-generator/flask-argon-dashboard.git
  $ cd flask-argon-dashboard
  ```

2. Initialize and activate a virtualenv:
  ```
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

4. Create the database, using Flask shell
  ```
  $ flask shell
  $ >>> from app import db
  $ >>> db.create_all()
  ```

5. Run the development server:
  ```
  $ flask run
  ```

6. See the running app by visiting [http://localhost:5000](http://localhost:5000) in your browser

<br />

## Features

- SQLite database
- Login, Register
- Static Build `python ./static.py`. The static build goes to `app/build` directory 
- FTP Deploy script. **Info**: this `require node.js` and the edit of `deploy.js` to add FTP server credentials. 

<br />

## Support

For issues and features request, use **Github** or access the [support page](https://appseed.us/support) provided by **AppSeed** 

<br />

## App Screenshots

![Flask Dashboard](https://github.com/app-generator/flask-argon-dashboard/blob/master/screenshots/flask-argon-dashboard-login.jpg)

<br />

![Flask Dashboard](https://github.com/app-generator/flask-argon-dashboard/blob/master/screenshots/flask-argon-dashboard-profile.jpg)

<br />

## Resources

 - [Flask Dashboard Argon](https://appseed.us/admin-dashboards/flask-dashboard-argon) - app info
 - Product [documentation](https://docs.appseed.us/admin-dashboards/flask-dashboard-argon/)
 - Live [DEMO](https://flask-argon-dashboard.appseed.us/)
 - Related [Blog Article](https://blog.appseed.us/flask-dashboard-argon-zero-to-full-stack/)
 - [Argon Dashboard](https://www.creative-tim.com/product/argon-dashboard) - design information (Creative-Tim)
 - [Flask](http://flask.pocoo.org/) - official website

<br />

---
[Flask Dashboard Argon](https://appseed.us/admin-dashboards/flask-dashboard-argon) provided by **AppSeed**
