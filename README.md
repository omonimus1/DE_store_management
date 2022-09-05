## ED Store

ED store is a management system  that allow a store managers to monitor
stock, offers, loyalty cards, and others managers all by one platform.

## Technologies, framework and tools Used
* Django
* HTML, CSS, Javascript, Bootstrap
* Github


# 🔗 Links  - [Get my Linktree](https://linktr.ee/davidepollicino) #

[![linked-in](https://img.shields.io/badge/Linked_In-0077B5?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://linkedin.com/in/davidepollicino7/)
[![github](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/omonimus1)
[![medium](https://img.shields.io/badge/medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://davidepollicino.medium.com/)
[![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=Gmail&logoColor=white)](mailto:davidepollicino2015@gmail.com)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/DavidePollicin.svg?style=social&label=Follow%20%40DavidePollicin)](https://twitter.com/DavidePollicin)


## Apply for a mentorship session with me (get a 7 days free trial)
<a href="https://mentorcruise.com/mentor/davidepollicino/"> <img src="https://cdn.mentorcruise.com/img/banner/navy-mentoring-badge.svg" width="240" alt="MentorCruise"> </a>


## Functionalities
#### User management: 
* Admin are able to login and create new authorized users by using the built-in Django admin dashboard. 
#### Sales preview:
* A manager will be able to view a sale preview related to the last 24 hours, week, months, trimester, year and total (in according to the full history present in the database).  
#### Product management: 
* View list of products.
* Edit product price and minimum stock needed before to have an alert.
* Receive an alert (email), once the product stock items would go under the minimum items.  
* View Information related to the Products, like ID, name, price, description, category, stock, minimum stock, status. 
#### Financial Verification: 
* Emulate the integration of a third-part service that will allows the manager to verify if a client is eligible for montly payment.
#### Offer: 
* A manager is able to create a new offer and view the total list of offer available  
#### Loyalty Card: 
View list of loyalty card with their relative status and information (card number, Owner full name, owner email, points accumulated in the card, activation date, state: active or not active). 
#### Logout: 
* To increase security levels, admins are able to logout once access to the platform is no longer needed and login back once needed. 

## System requisites
* Python3
* Pip
* Mailhog
## How to run 
```
cd mysite
source venv/bin/activate
python3 manage.py runserver
```
## Run unit tests
```
python3 manage.py test 
```

## Login
Make sure to create a user by the project admin section in order to login and get access to the dashboard. 

## Preview

### Login page
![Login](/media/login.png "Login Page")
### Sales Overview Page
![Sales](/media/sales.png "Sales Page")
### Product page
![Product](/media/product.png "product Page")
### Edit product
![Edit price](/media/edit-price.png "Edit product")

### Offer page
![Offer](/media/offer.png "Offer Page")

### Prototype integration third-part finance check service
![Finance](/media/finance.png "Finance")
