from random import *
class SitBooking:
    
    s_8={x for x in range(1,51)}
    s_12={x for x in range(1,51)}
    s_3={x for x in range(1,51)}
    s_7={x for x in range(1,51)}
    s_10={x for x in range(1,51)}
    ti={8.30 , 12.0 , 3.30 , 7.0 , 10.30}
    
    def __init__(self,sitno,time,Name,Mob):
        self.time=time
        self.Name=Name
        self.Mob=Mob
        self.sitno=sitno
    
    def choice(self): 
        if (self.time==3.3) and (self.sitno in SitBooking.s_3):
            def otp():
                return randint(1000,9999)
            OTP=otp()    
            print(OTP)
            x=int(input('Please Enter OTP : '))
            if (x==OTP):
                SitBooking.s_3.remove(self.sitno)
                print('Your Sit Is Booked')
            else:
                print('OTP Not Matched')
        elif (self.time==7.0) and (self.sitno in SitBooking.s_7):
            def otp():
                return randint(1000,9999)
            OTP=otp()    
            print(OTP)
            x=int(input('Please Enter OTP : '))
            if (x==OTP):
                SitBooking.s_7.remove(self.sitno)
                print('Your Sit Is Booked')
            else:
                print('OTP Not Matched') 
        elif (self.time==8.3) and (self.sitno in SitBooking.s_8):
            def otp():
                return randint(1000,9999)
            OTP=otp()    
            print(OTP)
            x=int(input('Please Enter OTP : '))
            if (x==OTP):
                SitBooking.s_8.remove(self.sitno)
                print('Your Sit Is Booked')
            else:
                print('OTP Not Matched') 
        elif (self.time==10.3) and (self.sitno in SitBooking.s_10):
            def otp():
                return randint(1000,9999)
            OTP=otp()    
            print(OTP)
            x=int(input('Please Enter OTP : '))
            if (x==OTP):
                SitBooking.s_10.remove(self.sitno)
                print('Your Sit Is Booked')
            else:
                print('OTP Not Matched')  
        elif (self.time==12.0) and (self.sitno in SitBooking.s_12):
            def otp():
                return randint(1000,9999)
            OTP=otp()    
            print(OTP)
            x=int(input('Please Enter OTP : '))
            if (x==OTP):
                SitBooking.s_12.remove(self.sitno)
                print('Your Sit Is Booked')
            else:
                print('OTP Not Matched')        
        else:
            print('Sorry This Sit Is Already Booked.. Please Book Other Sit Or Select Other Time Slot...')
            
    def know(self):
        if self.time==3.3:
            print(SitBooking.s_3)
        elif self.time==7.0:
            print(SitBooking.s_7)    
        elif self.time==8.3:
            print(SitBooking.s_8) 
        elif self.time==10.3:
            print(SitBooking.s_10)
        elif self.time==12.0:
            print(SitBooking.s_12)     
            
    def download(self):
        print('Name : ',self.Name)
        print('Mobile No : ',self.Mob)
        print('Time Slot : ',self.time)
        print('Sit Number : ',self.sitno)
        
        
print('Welcome To Online Sit Booking Platform') 
while 1:
    print('b-Booking \na-Available Sits \nd-Download Tickit \ne-Exit')
    option=input('Enter Your Option : ').lower()
    if option=='b':
        n=input('Enter Your Name : ')
        m=input('Enter Your Mobile Number : ')
        if (len(m)==10):
            print(SitBooking.ti)
            p=float(input('Enter Time From Above Mention Time Slots : '))
            if p in SitBooking.ti:
                Sit=int(input('Enter The Sit Number You Want To Book : '))    
                t=SitBooking(Sit,p,n,m)
                if t.sitno>50:
                    print('Please Enter Sit Number Between 0 To 50')
                else: 
                    t.choice()
            else:
                print('Please select Valid Time Slot')
            
        else:
            print('Please Enter Valid 10 Digit Number')
    elif option=='a':
        print(SitBooking.ti)
        t_i=float(input('Enter Time From Above Mention Time Slots : '))
        oo=SitBooking(None,t_i,None,None)
        oo.know()
    elif option=='d':
        t.download()
    elif option=='e':
        break
    else:
        print('Please Choose Valid Option')