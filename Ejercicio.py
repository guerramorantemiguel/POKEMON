import pandas as pd
datos = pd.read_csv("poke_mon.csv", header = 0)

id = list(datos["PokeDex_index_number"])
name = list(datos["Name_of_the_Pokemon"])
type_1 = list(datos["Type_of_pokemon"])
type_2 = list(datos["Other_Type_of_Pokemon"])
total = list(datos["Sum_of_Attack, Sp._Atk, Defense, Sp._Def, Speed_and_HP"])
HP = list(datos["Hit_Points"])
Attack = list(datos["Attack_Strength"])
Defense = list(datos["Defensive_Strength"])
SP_Atk = list(datos["Special_Attack_Strength"])
SP_Def = list(datos["Special_Defense_Strength"])
Speed = list(datos[""])

print("— CANTIDAD DE POKEMON --") 
n = id.count() 
print("Cantidad de pokemon = " + str(n)) 

def calculomedia(type_1):
  with open('poke_mon.csv') as csvarchivo:
    entrada = csv.DictReader(csvarchivo)
    for reg in entrada:
        print(reg['Grass'])
  t_g = Grass.count()  
  media = t_g/n
  print(media)
  with open('poke_mon.csv') as csvarchivo:
    entrada = csv.DictReader(csvarchivo)
    for reg in entrada:
        print(reg['Normal'])
  t_n = Normal.count()  
  media = t_n/n
  print(media)
