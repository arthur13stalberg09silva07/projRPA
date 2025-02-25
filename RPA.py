# import win32com.client as win32
# outlook = win32.Dispatch("outlook.application")
# email_out = outlook.CreateItem(0)
import win32com.client as win32
import os

outlook = win32.Dispatch("outlook.application")

email_out = outlook.CreateItem(0)
    
email_out.To = "email.teste@germinare.org.br"
email_out.Subject = "Email"  

email_out.HTMLBody = f"""
    <html>
        <body>
            <p>
                <a href="" target="_blank">Clique aqui para assistir ao vídeo</a>
            </p>
        </body>
    </html>
    """

email_out.Send()
print("E-mail enviado com sucesso!")

print("Todos os e-mails foram enviados!")
