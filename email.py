import win32com.client as win32
import os

caminho_arquivo = os.path.abspath("carros.xlsx")

outlook = win32.Dispatch("outlook.application")

email_out = outlook.CreateItem(0)

email_out.To = "arthur.stalberg@germinare.org.br"
email_out.Subject = "Email com Anexo"  

email_out.HTMLBody = f"""
    <html>
        <body>
            <p>
                <a href="" target="_blank">Clique aqui para assistir ao vídeo</a>
            </p>
        </body>
    </html>
    """

if os.path.exists(caminho_arquivo):
    email_out.Attachments.Add(caminho_arquivo)
else:
    print("O arquivo não foi encontrado!")

email_out.Send()
print("E-mail enviado com sucesso com o anexo!")