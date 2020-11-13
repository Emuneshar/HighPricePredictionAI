import smtplib

class Email_Info:
    def __init__(self, sender_email, receiver_email):    
        self.sender_email = sender_email
        self.receiver_email = receiver_email  

class Server(Email_Info):
    def __init__(self, email):
        self.email = email

    def send_email(self):
        pass
