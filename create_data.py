import requests
import pandas as pd

BASE = 'http://127.0.0.1:5000/'

# Create a session to maintain cookies
session = requests.Session()

users = pd.read_excel('./data.xlsx',sheet_name='User')
products = pd.read_excel('./data.xlsx',sheet_name='Product')

# Signup Users
for user in users.to_dict('records'):
    print(user)
    signup_response = session.post(BASE + 'signup',data=user)
    if signup_response.ok:
        print(f'{user["name"]} sign up')


# Login and Upload Product
for user_name in users['name'][1:]:
    user = {
        'email':user_name + '@gmail.com',
        'password':user_name
    }

    login_response = session.post(BASE + 'login',data=user)
    

    if login_response.ok:
        for product in products[products['Owner'] == user_name].to_dict('records'):
            upload_response = session.post(BASE + 'user_profile',data=product)
            if upload_response.ok:
                print('Upload success')