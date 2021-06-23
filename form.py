from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, DateField, FileField
from wtforms import validators


class SignUpForm(Form):
      fname = TextField("First Name ", [validators.required("Please enter your first name.")])
      lname = TextField("Last Name", [validators.required("Please enter your last name.")])
      add = TextAreaField("Address")
      city = TextField("City")
      pin = TextField("Pincode")
      contact = TextField("Contact Number")
      email = TextField("Email", [validators.required(message='Please enter your email address.'),
                                  validators.Email("Please enter your email address.")])
      userid = TextField("User ID", [validators.Required("Please enter your user id.")])
      password = PasswordField("Password", [validators.Required("Please enter your password.")])
      password2 = PasswordField("Re-type Password", [validators.Required("Please re-enter your password.")])
      lic_num = TextField("License Number")
      lic_val = DateField("License Validity")
      rto = TextField("RTO Circle")
      lic_front = FileField("License Front Side")
      lic_rear = FileField("License Rear Side")

      submit = SubmitField("Submit")
      submit1 = SubmitField("Next")





class LoginForm(Form):
      userid = TextField("User ID", [validators.Required("Please enter your user id.")])
      password = PasswordField("Password", [validators.Required("Please enter your password.")])
      submit = SubmitField("LOGIN")
      reg = SubmitField("Register Here")