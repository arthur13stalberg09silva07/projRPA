from banco import Banco
from planilha import Planilha
from RPA import Rpa
from email import sendEmail
def main():
    banco = Banco()
    cars = banco.get_all_carros()
    planilha = Planilha(cars)
    planilha.criar_planilha()
    rpa = Rpa(cars)
    path = rpa.executar()
    sendEmail(path)
    banco.close_connection()

if __name__ == '__main__':
    main()