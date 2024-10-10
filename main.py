from admin import  *
from login import  *
from user import  *

from list import  *



while True:
    print('''
1.register
2.login
3.exit
''')
    choice=int(input('enter your choice:'))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print('''
                1.add shoes
                2.view shoes
                3.ubdate shoes
                4.delete
                5.view user
                6.exit
                ''')
                sub_choice=int(input("enter the choice :"))
                if sub_choice==1:
                    add_shoes()
                elif sub_choice==2:
                    view_shoes()
                elif sub_choice==3:
                    ubdate_shoes()
                elif sub_choice==4:
                    delete()
                elif sub_choice==5:
                    view_user()
                elif sub_choice==6:
                    break
                else:
                    print('invalid')



            
        elif f==2:
            while True:
                print('''
                1.view profile
                2.ubdate profile
                3.view shoes
                4.buy shoes
        
               
                6.exit
                ''')
                sub_ch=int(input('enter the choice:'))
                if sub_ch==1:
                    view_profile(user)
                elif sub_ch==2:
                    ubdate_profile(user)
                elif sub_ch==3:
                    view_shoes()
                elif sub_ch==4:
                    buy_shoes(user)
          
                

                elif sub_ch==6:
                    break
                else:
                    print('invalid')
                


            
        elif f==0:
            print('invalid username or password')

    elif choice==3:
        break
    else:
        print('invalid')