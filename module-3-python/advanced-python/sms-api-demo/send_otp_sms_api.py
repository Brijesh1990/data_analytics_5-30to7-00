# send otp via call or send otp api demo
# request integrated api (application programming interface)
import requests
import random 
# otp providers api key
API_KEY="caf9ee1e-ae55-11f1-90d7-0200cd936042"
# receiver phone numbers
phone="917984266511"
# generate OTP via random function
otp=str(random.randint(100000,999999))
# otp providers
url=f"https://2factor.in/API/V1/{API_KEY}/SMS/{phone}/{otp}"

# send OTP vi python script using exception handling
try:
    response=requests.get(url)
    print("status code :",response.status_code)
    print("Response :",response.text)
    
    if response.status_code==200:
        print("Otp send successfully")
        # asked user to enter OTP
        entered_otp=input("Enter your OTP here :")
        # checked otp right or wrong 
        if entered_otp==otp:
            print("your otp entered successfully authenticated")
        else:
            print("you entered a wrong otp try again")
            
except requests.exceptions.RequestException as e:
    print('Something went wrong while sending OTP or SMS',e)

# finally:
#     print("something wrong in server please check your setting of sms api for OTP")
     

 
