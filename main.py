from banco import Banco
from planilha import Planilha
from RPA import Rpa
from EMAIL import sendEmail
def main():
    banco = Banco()
    cars = banco.get_all_carros()
    planilha = Planilha(cars)
    planilha.criar_planilha()
    rpa = Rpa(cars)
    path = rpa.executar()
    sendEmail(path)


if __name__ == '__main__':
    main()