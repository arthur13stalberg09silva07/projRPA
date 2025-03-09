from banco import Banco
from planilha import Planilha
from rpa import Rpa

def main():
    banco = Banco()
    cars = banco.get_all_carros()
    planilha = Planilha(cars)
    planilha.criar_planilha()
    rpa = Rpa(cars)
    rpa.executar()

if __name__ == '__main__':
    main()