import pandas as pd
datos = pd.read_csv("poke_mon.csv", header = 0)

id = list(datos["PokeDex_index_number"])
name = list(datos["Name_of_the_Pokemon"])
type_1 = list(datos["Type_of_pokemon"])
type_2 = list(datos["Other_Type_of_Pokemon"])
total = list(datos["Sum_of_Attack, Sp._Atk, Defense, Sp._Def, Speed_and_HP"])