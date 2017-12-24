## Project 4: Item Catalog - Sports Gear App

### Description of The Project

>You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

>You will learn how to develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. You will then learn when to properly use the various HTTP methods available to you and how these methods relate to CRUD (create, read, update and delete) operations.

### Required Software

1. [python](https://www.python.org/downloads/)
2. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
3. [Vagrant](https://www.vagrantup.com/downloads.html)
4. [VM Configuration](http://github.com/udacity/fullstack-nanodegree-vm)

### Computer Setup

1. Install __python__, __VirtualBox__ and __Vagrant__.
2. Clone the __VM Configuration__ files(It may be located in your downloads folder).  This file gives you a folder named __fullstack-nanodegree-vm__ that contains the VM configuration files.
3. clone the **catalog folder** from the repository [here](https://github.com/crensma11/sport_gear_app).  The folder inside is called **catalog** and will need to be located in the **vagrant** directory which is located in the previously downloaded folder **fullstack-nanodegree-vm**.

### Project Files

The project contains three (3) main files:

1. *application.py* - contains the Python program that is used to run the item catalog application.
2. *database_setup.py* - contains the database setup code.
3. *lotsofgear.py* - this file is used to populate the database file with the items in the catalog.

### How To Execute The Project

1. The first thing we need to do is bring the virtual machine online and then log into it.  We will need to be in the **vagrant** directory to do this.  Remember the **vagrant** directory is located in the folder **fullstack-nanodegree-vm**.  We also need to cd into the shared folder between the virtual machine and the host machine in order to see the files for the project.
Execute these commands from the terminal:

```
fullstack-nanodegree-vm
$ cd vagrant

vagrant
$ vagrant up

vagrant
$ vagrant ssh

vagrant@vagrant:~$ cd /vagrant
```

2. While in the **catalog** folder execute the **database_setup.py** to build the database and then execute **lotsofgear.py** to populate the database with the initial item information.  Execute these commands:

```
vagrant@vagrant:/vagrant$ cd catalog

vagrant@vagrant:/vagrant/catalog$ python database_setup.py

vagrant@vagrant:/vagrant/catalog$ python lotsorgear.py

```

3. To start the application the **application.py** file has to be executed and then you can visit the http://localhost:8000 from your local browser and explore the app.   Execute this command:

```
vagrant@vagrant:/vagrant/catalog$ python application.py
```

### Using Google or Facebook Login
To get the Google Login working, these steps need to be followed:

1. Go to [Google Developers Page](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Credentials > OAuth Client ID
5. Select Web application
6. Enter name 'Sport Gear App'
7. Authorized JavaScript origins = 'http://localhost:8000'
8. Authorized redirect URIs = 'http://localhost:8000/login' && 'http://localhost:8000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory.

To get the Facebook Login working, these steps need to be followed:

1. Go to [Facebook Developers Page](https://developers.facebook.com/)
2. Sign up or login if prompted
3. Follow the step to create a web application.
4. Click + Add Product in the left column.
5. Find Facebook Login in the Recommended Products list and click Set Up.
6. Click Facebook Login that now appears in the left column.
Add http://localhost:8000/ to the Valid OAuth redirect URIs section.
7. Copy the Client ID and paste it into the `appId` in login.html
8. On the Dev Console Select Download JSON
9. Rename JSON file to fb_client_secrets.json
10. Place JSON file in the catalog directory.

### Created By *Adam Crenshaw*
