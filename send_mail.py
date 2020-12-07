from decouple import config
import smtplib

EMAIL_ADDRESS_SENDER= config('SENDER.EMAIL')
EMAIL_ADDRESS_RECIPIENT= config('RECIPIENT.EMAIL')
EMAIL_KEY= config('KEY')

def send_mail():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    type(smtpObj)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(EMAIL_ADDRESS_SENDER, EMAIL_KEY)
    smtpObj.sendmail(EMAIL_ADDRESS_SENDER, EMAIL_ADDRESS_RECIPIENT, 'Subject: This is a Test \n')

send_mail()
