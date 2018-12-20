import os
import smtplib
import sys


class PyMail(object):
    def __init__(self, sender='elvisrodriguez1992@gmail.com'):
        self.sender = sender
        self.password = None
        self.handler = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        self.message = None
        self.STATUS_CODES = [235, 250]

    def create_message(self, subject='', message=''):
        email = 'Subject: {subject}\n{message}'.format(subject=subject,
                                                       message=message)
        self.message = email

    def send_email(self, recepient):
        if self.message is None:
            print('Message not created yet')
            return
        connection = self.handler.ehlo()
        if connection[0] in self.STATUS_CODES:
            print('Connection Status: OK')
            self.password = str(input('Password:'))
            login = self.handler.login(self.sender, self.password)
            if login[0] in self.STATUS_CODES:
                print('Login Successful')
                self.handler.sendmail(self.sender, recepient, self.message)
                print('Email sent, closing connection...')
                self.handler.quit()


if __name__ == '__main__':
    gmail_obj = PyMail()
    message = 'This is a test. Email script wrapped in a class.'
    gmail_obj.create_message(subject='Testing', message=message)
    gmail_obj.send_email(recepient='elvisrodriguez1992@gmail.com')
