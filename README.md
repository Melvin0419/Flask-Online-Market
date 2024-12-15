# Flask Online Market
This web application allows users to purchase goods on the website. Users can sign up for an account to add products to their cart, and uploading their products is also allowed.

## Main Page Intro
* **Home Page**
  
   Shows all product information, including the product's name, description, and cost. Sorting and keyword filtering are provided.
* **Sign-up / Log-in Page**
  
   It allows users to create and log in to their accounts. Some pages can only be accessed with logged-in status.

* **User Profile Page**

   This page shows the user's information, including name, email, and the table of uploaded products. Account information is allowed on this page.

* **User Product Page**

   This page allows users to upload their products to sell. The uploaded products are shown here, too.
  
* **Product Profile Page**

   It shows detailed information about the product, including its name, description, cost, and owner's name. Users who have bought this product will also have their names shown under the product information.

* **Cart Page**

   Shows products that are added to the cart. Any change to the cart (add new products, remove products) is allowable.

* **Admin Page**

   This page is specifically for the administrator(admin should be selected in the role options when signing up for an account). All the registered accounts and uploaded products are shown on this page. The administrator can directly delete the user instance or the product instance.


## How to run this web application
1. Clone this repo to the local side and install necessary packages(check `requirements.txt`)
2. Execute `main.py` to activate the server.
3. To quickly experience this web app, use `create_data.py` to add `User` and `Product` instances to the database. The script will automatically grab the data from `data.xlsx` and then create instances.
4. Visit the local URL and start to create your account and purchase something good.


![image](https://github.com/user-attachments/assets/cf14fa44-5a89-40ae-b487-c43a49aa3979)

## Visit the online website
This web application is deployed on Heroku, click the above URL to visit the website.

https://flask-online-market-2dce5e8d9d83.herokuapp.com/
