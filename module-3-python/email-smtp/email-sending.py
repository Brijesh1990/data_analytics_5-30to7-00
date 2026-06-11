# import smtp email package is inbuild package provided by python 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# send email to reciever and sender details 
sender_email="brijeshpandey.tops@gmail.com"
receiver_email="bkpandey.pandey@gmail.com"
apppassword=""

# create email services to send email
message=MIMEMultipart()
message["From"]=sender_email
message["to"]=receiver_email
message["subject"]="For sending email using python inbuild module"

# email text 

# body="Hello : \n \n \n THis is a email testing to send email via python using smtplib"

body="Hello : \n \n \n THis email from tops technologies pvt limited download our brochures as attached find following"
message.attach(MIMEText(body,"plain"))

# used exceptions handeling ...
file_path="da.pdf"
try:
    #connect to send email with gmail server 
    # open a file via file handeling 
    with open(file_path,"rb") as attachment:
        part=MIMEBase("application","octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        # attachments web formate send read 
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file_path}"
        )
        message.attach(part)
        
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls() 
    server.login(sender_email, apppassword)
    
    # send email 
    server.sendmail(
        sender_email,
        receiver_email,
        message.as_string()
    )
    # print a message 
    print("Your email successfully send please check receiver email")

except Exception as e:
    print("Something went wrong", e)
    
finally:
    server.quit()

