import requests
import random

# create a 6 or 7 digit random OTP 
otp=random.randint(100000, 999999)
# send otp on that numbers that can not be in DND 
mobile="998003879"

# applied third party inetegration twilio | way2sms | fast2sms etc
url="https://www.fast2sms.com/dev/bulkV2"

payload={
    "route":"otp",
    "variable_values":otp,
    "numbers":mobile
}

headers={
    "authorization":"paste your api key"
} 


# get response of sms API via fast2sms 
response=requests.post(url,data=payload, headers=headers)
print("OTP is generated successfully",otp)
print(response.text)