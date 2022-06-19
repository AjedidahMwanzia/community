# community

>[AjedidahMwanzia](https://github.com/AjedidahMwanzia)  
  
# Description  
Tis is a neighborhood app where a user must signup first, be able to join a hood owned by the hood admin, and once you 
join a hood, one can see businesses and posts in only that wood they belong to.  
##  Live Link  
 Click [View Site]()  to visit the site
  
## Screenshots 
###### Home page
 
<!-- <img src="https://ucarecdn.com/457f313d-4181-4d86-aca7-a91151d80707/hood.png"> -->

 
## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/AjedidahMwanzia/community
```
##### Navigate into the folder and install requirements  
 ```bash 
cd community 
```
##### Install and activate Virtual  
 ```bash 
- pipenv shell
```  
##### Install Dependencies  
 ```bash 
 pipenv install requests
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations community
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   


-   Email- [Ajedidah Mwanzia](mailto:ajedidah.mwanzia@student.moringaschool.com)
-   Linkedin - [Ajedidah Mwanzia](https://www.linkedin.com/in/ajedidah-mwanzia/)
-   Portfolio - [Ajedidah Mwanzia](https://ajedidahmwanzia.github.io/portfolio/)
  
## License 

* *MIT License:*
* Copyright (c) 2022 **Ajedidah Mwanzia**

[Go Back to the top](#community)
