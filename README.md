# Flask Online Market
This web application allows users to purchase goods on the website. Users can sign up for an account to add products to their cart, and uploading their products is also allowed.

## Main Page Intro
* **Home Page**
  
   Shows all product information, including the product's name, description, and cost.
* **Sign-up / Log-in Page**
  
   Allows users to create their accounts / log in their accounts. Some pages can only be accessed with logged-in status.

* **User Profile Page**

   This page shows the user's information, including name, email, and products that are uploaded by themself. This page also allows users to upload their products to sell.
* **Product Profile Page**

   Shows detailed information about the product including the product's name, description, cost, and the owner's name. Users who have bought this product, their name will also be shown under the product information.

* **Cart Page**

   Shows products that are added to the cart. Any change to the cart (add new products, remove products) is allowable.

## How to run this web application
1. Clone this repo to the local side and install necessary packages(check `requirements.txt`)
2. Execute `main.py` to activate the server.
3. To quickly experience this web app, use `create_data.py` to add `User` and `Product` instances to the database. The script will automatically grab the data from `data.xlsx` and then create instances.
4. Visit the local URL and start to create your account and purchase something good.


![image](https://github.com/user-attachments/assets/ac79644e-2a31-4689-8aa4-e12599bcd9cd)

## Visit the online website
This web application is deployed on Heroku, click the above URL to visit the website.

https://flask-online-market-2dce5e8d9d83.herokuapp.com/
