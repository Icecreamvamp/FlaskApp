from flask.ext.wtf import Form
from wtforms import StringField, SubmitField 

class OrderForm(Form):
    naam = StringField("Naam:")
    email = StringField("Email:")
    straat = StringField("Straat:")
    postcode = StringField("Postcode:")
    telefoon = StringField("Telefoon:")
    code = StringField("Code:")
    submit = SubmitField("Submit")
