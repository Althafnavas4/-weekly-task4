from login import  *
from user import  *
from list import  *
def add_shoes():
    if len(lib)==0:
        id=1
    else:
        id=lib[-1]['id']+1
    f1=0
    for i in lib:
        if i['id']==id:
            f1=1
            add_shoes()
    
   
    name=str(input("enter the name :"))
    price=int(input("enter the  price:"))
    stock=int(input('enter the stock:'))
    size=int(input('enter size'))
    lib.append({'name':name,'price':price,'stock':stock,'size':size,'id':id})
def view_shoes():
    print(lib)
def ubdate_shoes():
    id=int(input('enter id :'))                                                         
    f1=0
    for i in lib:
        if i['id']==id:
            f1=1
            price=int(input('enter price :'))                                   
            stock=str(input('enter stock :'))
            i['price']=price
            i['stock']=stock
    if f1==0:
        print('invalid id')
    
def delete():
    id=int(input('enter id :'))
    f1=0
    for i in lib:
        if i['id']==id:
            f1=1
            lib.remove(i)

    if f1==0:
        print('invalid id')


def  view_user():
    for i in user_dtls:
        print('name',i['name'])
        print('id',i['id'])
        print('email',i['email'])
        print('phone',i['phone'])
            