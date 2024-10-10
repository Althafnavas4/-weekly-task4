user_dtls=[]
lib=[]

def register():
    if len(user_dtls)==0:
        id=100
    else:
        id=user_dtls[-1]['id']+1
    print(id)

    email=str(input("enter the email :"))
    f1=0
    for i in user_dtls:
        if i['email']==email:
            f1=1
            register()
    if f1==0:
    
            name=str(input("enter the name :"))
            phone=int(input("enter the  phone number:"))
            username=email
            password=input('enter the password:')
            user_dtls.append({'name':name,'id':id,'phone':phone,'email':email,'password':password,'books':[]})

def login():
    uname=input('enter username:')
    passw=input('enter password:')
    f=0
    if uname=='admin' and passw=='admin':
        f=1
    user=''
    for i in user_dtls:
        if uname==i['email'] and passw==i['password']:
            f=2
            user=i
    return f,user