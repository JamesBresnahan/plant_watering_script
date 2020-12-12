from decouple import config
import smtplib

EMAIL_ADDRESS_SENDER= config('SENDER.EMAIL')
EMAIL_ADDRESS_RECIPIENT= config('RECIPIENT.EMAIL')
EMAIL_KEY= config('KEY')

def send_reading_mail(plant, reading):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    type(smtpObj)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(EMAIL_ADDRESS_SENDER, EMAIL_KEY)
    message_subject = 'Subject: ' + plant + ' has a current moisture level of ' + reading
    smtpObj.sendmail(EMAIL_ADDRESS_SENDER, EMAIL_ADDRESS_RECIPIENT, message_subject)

send_reading_mail('dill', '111')
