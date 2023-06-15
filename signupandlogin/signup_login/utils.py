# from django.core.mail import EmailMessage
# from django.conf import settings


# class Util:
#     @staticmethod
#     def send_email(data):
#         email = EmailMessage(
#             subject=data["subject"],
#             body=data["body"],
#             from_email=settings.EMAIL_HOST_USER,
#             to=[data["to_email"]],
#         )
#         email.send()


from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
import base64


def string_b64encode(string):
    bytes_encoded = string.encode("ascii")
    # print(bytes_encoded)
    # print(type(bytes_encoded))
    # print(urlsafe_base64_encode(bytes_encoded))
    return urlsafe_base64_encode(bytes_encoded)


def string_b64decode(bytesstr):
    str_decoded = urlsafe_base64_decode(bytesstr)
    # print(str_decoded)
    string = str_decoded.decode()
    # print(string)
    return string


def send_email(user):
    to = user.email
    name_f = user.first_name
    name_l = user.last_name
    name = name_f + " " + name_l
    uid = urlsafe_base64_encode(force_bytes(user.id))

    subject = "Welcome to Real Returns Project"
    values = "<p>Hello #NAME#,</p><p>Your account has been created.</p><p>Your login credentials :</p><p>Email: #EMAIL#</p><p>Please click the link to verify your email.</p><p>Thank you,</p><p>&nbsp;</p>"
    values = values.replace("#NAME#", name)
    values = values.replace("#EMAIL#", to)

    activation_link = (
        "http://127.0.0.1:8000/emailactivate/" + uid + "/" + user.verify_string
    )

    html_content = render_to_string(
        "verify_email.html", {"content": values, "content1": activation_link}
    )

    email = EmailMultiAlternatives(
        subject, html_content, settings.EMAIL_HOST_USER, [to]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()


def send_resetpasswordemail(user, token):
    to = user.email
    print(to)
    name_f = user.first_name
    name_l = user.last_name
    name = name_f + " " + name_l
    # print(token)
    # token = PasswordResetTokenGenerator().make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.id))
    # print(uid)

    subject = "Reset Password"
    values = "<p>Hello #NAME#,</p><p>Email: #EMAIL#</p><p>Please click on the button to change the password.</p><p>Thank you,</p><p>&nbsp;</p>"
    values = values.replace("#NAME#", name)
    values = values.replace("#EMAIL#", to)

    Resetpassword_link = "http://127.0.0.1:8000/resetpassword/" + uid + "/" + token

    html_content = render_to_string(
        "email_resetpassword.html", {"content": values, "content1": Resetpassword_link}
    )

    email = EmailMultiAlternatives(
        subject, html_content, settings.EMAIL_HOST_USER, [to]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()


def send_changeemail(user, email, token):
    to = email
    print(to)
    name_f = user.first_name
    name_l = user.last_name
    name = name_f + " " + name_l
    uid = urlsafe_base64_encode(force_bytes(user.id))
    token1 = string_b64encode(email)

    subject = "'Account Email Change Request'"
    values = "<p>Hello #NAME#,</p><p>Email: #EMAIL#</p><p>Please click the link to verify your new email.After Successful verification you can use your new email to login</p><p>Thank you,</p><p>&nbsp;</p>"
    values = values.replace("#NAME#", name)
    values = values.replace("#EMAIL#", to)

    activation_link = (
        "http://127.0.0.1:8000/changeemail/" + uid + "/" + token + "/" + token1
    )

    html_content = render_to_string(
        "verify_email.html", {"content": values, "content1": activation_link}
    )

    email = EmailMultiAlternatives(
        subject, html_content, settings.EMAIL_HOST_USER, [to]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
