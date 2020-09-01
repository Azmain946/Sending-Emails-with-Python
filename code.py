import smtplib,ssl
# set up the SMTP server
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
message = MIMEMultipart("alternative")

n=int(input()) #how much email do you want to send
report_file = open('') #locate the html code here
html = report_file.read()

sender = '' #enter your email
receivers = [] #enter recievers email
message["Subject"] = "This email has been sent with Python"
message["From"] = sender
message["To"] = receivers




part2 = MIMEText(html, "html")

message.attach(part2)

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(Your email, Your Password)
for i in range(n):
	s.send_message((message))         
	print("Successfully sent email")
