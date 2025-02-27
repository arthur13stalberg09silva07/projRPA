import pandas as pd
class Planilha:
    def __init__(self, carros: pd.DataFrame):
        self.__dt = pd.DataFrame(carros)
    
    def criar_planilha(self):
        return self.__dt.to_excel("carros.xlsx")
    
    def get_dt(self):
        return self.__dt