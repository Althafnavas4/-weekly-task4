from admin import  *
from login import  *
from list import  *

def  view_user():
    for i in user_dtls:
        print('name',i['name'])
        print('id',i['id'])
        print('email',i['email'])
        print('phone',i['phone'])
            
def view_profile(user):
    print(user)
    
def ubdate_profile(user):
    name=str(input("enter the name :"))
    phone=int(input("enter phone no :"))
    user['name']=name
    user['phone']=phone
def view_shoes():
    print(lib)
def buy_shoes(user):
    id=int(input('enter the id:'))
    f=0
    for i in lib:
        if i ['id']==id:
            f=1
            i['stock']-=1
            user['shoes'].append(id)
            print('shoes added')
        if f==0:
            print('invlid')
