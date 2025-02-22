from operator import truediv
import random

def is_getalgeraden(gok, geheim_nummer ):
   if gok == geheim_nummer:
       print("correct")
       return True
   else:
       print("fout")
       return False

def raad_het_getal(bovengrens):
    geheim_nummer = random.randit(1, bovengrens)
    einde_spel = False
    gok =int(input("geef een getal"))
    geraden = is_getal_geraden (gok, geheim_nummer)
    if geraden == True:
        einde_spel = True
        raad_het_getal(10)


