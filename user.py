# def  view_user():
#     for i in user_dtls:
#         print('name',i['name'])
#         print('id',i['id'])
#         print('email',i['email'])
#         print('phone',i['phone'])
            
# def view_profile(user):
#     print(user)
    
# def ubdate_profile(user):
#     name=str(input("enter the name :"))
#     phone=int(input("enter phone no :"))
#     user['name']=name
#     user['phone']=phone
# def view_book():
#     print(lib)
# def lend_book(user):
#     id=int(input('enter the id:'))
#     f=0
#     for i in lib:
#         if i ['id']==id:
#             f=1
#             i['stock']-=1
#             user['books'].append(id)
#             print('book added')
#         if f==0:
#             print('invlid')

# def return_book(user):
#     id=int(input('enter the id:'))
#     f=0
#     for i in lib:
#         if i ['id']==id and id in user['books']:
#             f=1
#             i['stock']+=1
#             user['books'].remove(id)
#             print('book removed')
#         if f==0:
#             print('invlid')

# def book_in_hand(user):
#     print(user['books'])