import pyautogui as au
from time import sleep
class Rpa:
    def __init__(self, cars):
        self.__cars = cars

    def executar(self):
        self.__abrir_excel()
        self.__abrir_planilha()
        self.__escrever_cabecalho()
        self.__digitar_modelos()

    def __abrir_excel(self):
        au.press("winleft")
        sleep(3)

        au.write("excel")
        sleep(2)

        au.press("enter")
        sleep(2)

    def __abrir_planilha(self):
        au.press("enter")
        sleep(1)

        au.press("enter")
        sleep(1)
        au.press("tab")
        sleep(1)

    def __escrever_cabecalho(self):
        au.write("Modelo")
        au.press("tab")
        sleep(1)

        au.write("Ano de lançamento")
        au.press("tab")
        sleep(1)

        au.write("Cor")
        au.press("tab")
        sleep(1)

        au.write("Empresa")
        sleep(1)

    def __digitar_modelos(self):
        for cars in self.__cars:
            au.hotkey("ctrl", "left")
            sleep(0.5)

            au.press("enter")
            sleep(0.5)

            au.write(cars["modelo"])
            sleep(0.5)
            au.press("tab")
            sleep(0.5)

            au.write(str(cars["ano_lancamento"]))
            sleep(0.5)
            au.press("tab")
            sleep(0.5)

            au.write(cars["cor"])
            sleep(0.5)
            au.press("tab")
            sleep(0.5)

            au.write(cars["empresa"])
            sleep(0.5)