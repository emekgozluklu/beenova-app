# website
Beenova Web Application

INSTALL
-------

* Clone project from git
* Create virtual environment: `virtualenv venv -p python3.9`
* Switch to virtual environment: `source venv/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Initialize database: `flask --app beenova_app init-db`
* Run application: `flask --app beenova_app run`

Optional:
* Add mock data:
  * `sqlite3 instance/beenova.sqlite`
  * `.read beenova_app/insert_mock_data.sql`

DEPLOYMENT
----------
* Will be updated!

LICENSE
-------

    Copyright 2018 Beenova <emek@beenova.de>
    Licensed under the MIT License.

AUTHORS
-------

* Emek Gozluklu <emek@beenova.de> - Code
* Ufuk Yarisan <ufuk@beenova.de> - Code
