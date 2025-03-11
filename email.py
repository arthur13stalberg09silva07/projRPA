import win32com.client as win32
import os

def sendEmail(message):
        caminho_arquivo = os.path.abspath("carros.xlsx")

        outlook = win32.Dispatch("outlook.application")

        email_out = outlook.CreateItem(0)

        email_out.To = "matheus.melo@germinare.org.br"
        email_out.Subject = "Email com Anexo - Planilha de Carros"  

        email_out.HTMLBody = f"""
        <html>
            <body>
                <p>Olá,</p>
                <p>Segue a planilha de carros anexada.</p>
                <p>Atenciosamente,</p>
            </body>
        </html>
        """

        if os.path.exists(caminho_arquivo):
            email_out.Attachments.Add(caminho_arquivo)
        else:
            print("O arquivo não foi encontrado!")

        email_out.Send()
        print("E-mail enviado com sucesso com o anexo!")