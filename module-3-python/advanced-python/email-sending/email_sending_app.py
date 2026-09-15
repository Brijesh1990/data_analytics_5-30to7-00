# send email import smtplib 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import random
# add sender or receiver details to send email 
sender_email='brijeshdeveloper36@gmail.com'
receiver_email='krishlunagariya303@gmail.com'
apppassword=""
# send email text 
message=MIMEMultipart()
message["from"]=sender_email
message["to"]=receiver_email
message["subject"]="For sending email via python"
# body="Hello Everyone \n Please be continue right now and be practiced and revised all Things again \n Best Regards .....\n Brijesh Kumar pandey"
otp=str(random.randint(100000,999999))
body=otp
message.attach(MIMEText(body,"plain"))
# used exception handling to send email 
file_path="logo.png"
try:
    # connect to send email with gmail server
    with open(file_path,"rb") as attachment:
        part=MIMEBase("application","octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file_path}"
        )
        message.attach(part)
    
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,apppassword)
    # send email via sendmail()
    server.sendmail(
        sender_email,
        receiver_email,
        message.as_string()
    )
    if body==otp:
        print("Otp send successfully in your email :")
        entered_otp=input("Enter your OTP here :")
        # checked otp right or wrong 
        if entered_otp==otp:
         print("your otp entered successfully authenticated")
        else:
         print("you entered a wrong otp try again")
   
    
except Exception as e:
    print("your email not send successfully",e)
    
finally:
    server.quit()



