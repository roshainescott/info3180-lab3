from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY']='accessgranted'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT']='2525'
app.config['MAIL_USERNAME']='0000'
app.config['MAIL_PASSWORD']='0000'

mail=Mail(app)

from app import views