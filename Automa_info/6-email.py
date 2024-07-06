import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

#1- dados do e-mail
password = open("Automa_info\Senha", "r").read()
from_email = "email.com@gmail.com"
to_email = "email_qualquer@gmail.com"
subject = "Teste de e-mail"
# """ <- string multlinhas
body = """
Olá, segue e-mail teste
1
2
3
4
Teste
5
6
7
Atenciosamente,
"""
#2 - montando a estrutura do e-mail
message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()

#3 - adicionar anexo
anexo = "Teste.xlsx"
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split("/")
with open(anexo, "rb") as a:
    message.add_attachment(
        a.read(),
        maintype = mime_type,
        subtype = mime_subtype,
        filename = anexo
    )

#4 - envio do e-mail
with smtplib.SMTP_SSL("smpt.gmail.com", 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )