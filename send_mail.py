import config
import smtplib
import tagdata


def send():
    sender = "RaspberryPi"
    receiver = "Erik"
    subject = "Otsikko"


    message_text = tagdata.get()

    #parse to email
    message = f"From: {sender} <{config.SENDER_EMAIL}>" + "\n" + f"To: {receiver} <{config.RECEIVER_EMAIL}>" + "\n" + f"Subject: {subject}" + "\n" + "\n" + f"{message_text}"
    

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.ehlo()
        server.login(config.SENDER_EMAIL,config.PASSWORD)
        server.sendmail(config.SENDER_EMAIL, config.RECEIVER_EMAIL, message)
        server.close()
        
        print(f"Message sent successfully to {config.RECEIVER_EMAIL}")
    except:
        print("something went wrong")

send()
