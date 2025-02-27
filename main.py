from banco import Banco
from planilha import Planilha

def main():
    banco = Banco()
    carros = banco.get_all_carros()
    planilha = Planilha(carros)
    planilha.criar_planilha()

if __name__ == '__main__':
    main()