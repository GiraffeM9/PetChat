import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# regular sign in password = Md9MSB0Lq*&2
# APP PASSWORD = wmvnmvleqiavmxzm

sender_email = "petchatnet@gmail.com"
# users = ['mayita9d@yahoo.co.uk', 'mayitad9@hotmail.com']
password = "wmvnmvleqiavmxzm"

message = MIMEMultipart("alternative")
message["From"] = sender_email


def send_email(subject, users, msg):
    # Create secure connection with server to send email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        if len(users) <= 1:
            for i in range(len(users) - 1):
                # Create the plain-text and HTML version of your message
                username = users[i].username
                user_mail = users[i].mail

                part1, part2 = create_message(user_mail, subject, username, msg)

                # Add HTML/plain-text parts to MIMEMultipart message
                # The email client will try to render the last part first
                message.attach(part1)
                message.attach(part2)

                # send mail
                server.sendmail(
                    sender_email, user_mail, message.as_string()
                )
            else:
                username = users[0].username
                user_mail = users[0].email

                part1, part2 = create_message(user_mail, subject, username, msg)

                # Add HTML/plain-text parts to MIMEMultipart message
                # The email client will try to render the last part first
                message.attach(part1)
                message.attach(part2)

                # send mail
                server.sendmail(
                    sender_email, user_mail, message.as_string()
                )



def create_message(user_mail, subject, username, msg):

    message["To"] = user_mail
    message["Subject"] = subject

    text = f"""\
            Hello {username},
            {msg}
            Have a good day :) 
            - PetChat Team"""

    # finds path for html template
    for root, dirs, files in os.walk(r'Petchat/Website'):
        for name in files:
            print(name)
            if name == "email_template.html":
                path = os.path.abspath(os.path.join(root, name))

    with open(path, "r", encoding='utf-8') as html_file:
        html = html_file.read()
        html = html.replace("[username]", username)
        html = html.replace("[message]", msg)
        print(html)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    return part1, part2
