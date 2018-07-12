# Item Catalog Web App
This web app is a project for the Udacity FSND Course.

## About

This project is a RESTful web application utilizing the Flask framework which accesses a SQL database that populates categories and their items. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

## In This Project
This project has one main Python module views.py which runs the Flask application. A SQL database is created using the database_setup.py module and you can populate the database with test data using catalogitems.py. The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application.

## Skills Honed
1. Python
2. HTML
3. CSS
4. OAuth
5. Flask Framework
## Installation
 There are some dependancies and a few instructions on how to run the application. Seperate instructions are provided to  get GConnect working also.

## Dependencies
1. [Vagrant](https://www.vagrantup.com/)
2. [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
3. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
## How to Install
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip there
4. Launch the Vagrant VM (```vagrant up```)
5. Log into Vagrant VM (```vagrant ssh```)
6. Navigate to ```cd /vagrant``` as instructed in terminal
7. Setup application database ```python /catalog_app/database_setup.py```
8. Insert fake data ```python /catalog_app/catalogitems.py ```
9. Run application using ```python /catalog_app/views.py```
10. Access the application locally using 'http://localhost:5000'


## Using Google Login
To get the Google login working there are a few additional steps:

1. Go to Google Dev Console
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'Item-Catalog'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the data-clientid in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory that you cloned from here
14. Run application using python /item-catalog/app.py

## JSON Endpoints

The following are open to the public:
* catalogJSON: ```/catalog/JSON``` - Displays the whole catalog.
* ItemJSON: ```/catalog/<int:game_id>/item/<int:item_id>/JSON``` - Displays a particular items
* catalogitemJSON: ```/catalog/<int:game_id>/item/JSON``` - Displays items for a specific category
