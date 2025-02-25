from banco import Banco
import pandas as pd

banco = Banco()

pd.DataFrame(banco.get_all_carros()).to_excel("resultado.xlsx")