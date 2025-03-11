from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do Chrome em modo Headless (sem interface gráfica)
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=options)

# Acessa o Gmail
driver.get("https://mail.google.com/")

# Aguarda até o campo de email aparecer
wait = WebDriverWait(driver, 10)
email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
email_input.send_keys("arturnascimentosousa@gmail.com")
email_input.send_keys(Keys.RETURN)

# Aguarda a transição para o campo de senha
password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_input.send_keys("Ans060608")
password_input.send_keys(Keys.RETURN)

# Clicar no botão "Escrever"
compose_button = driver.find_element(By.XPATH, "//div[text()='Escrever']")
compose_button.click()
time.sleep(2)

# Preencher o destinatário
to_field = driver.find_element(By.NAME, "to")
to_field.send_keys("matheus.melo@germinare.org.br")

# Preencher o assunto
subject_field = driver.find_element(By.NAME, "subjectbox")
subject_field.send_keys("Assunto do E-mail")

# Preencher o corpo do e-mail
body_field = driver.find_element(By.XPATH, "//div[@aria-label='Corpo da mensagem']")
body_field.send_keys("Este é um e-mail enviado via automação.")

# Clicar no botão "Enviar"
send_button = driver.find_element(By.XPATH, "//div[text()='Enviar']")
send_button.click()

print("E-mail enviado com sucesso!")

driver.quit()