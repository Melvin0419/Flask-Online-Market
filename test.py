import requests

# BASE = 'http://127.0.0.1:5000/'
BASE = 'https://flask-online-market-c7ff847298d9.herokuapp.com/'

# Create a session to maintain cookies
session = requests.Session()

user1 = {
    'email':'melvin@gmail.com',
    'password':'melvin'
}

login_response = session.post(BASE + 'login', data=user1)
if login_response.ok:
    print("Login successful!")


# #加入購物車

# for i in range(3):
#     cart_response = session.post(BASE + 'addtocart', data={'product_id':i+1})
#     print(cart_response.json())

# 從購物車移除

# for i in range(3):
#     cart_response = session.post(BASE + 'rmfromcart', data={'product_id':i+1})
#     print(cart_response.json())
