# Maak een functie tic_tac_toe(), die ons hele hoofdprogramma bevat
from startcode.tictactoe.mytictactoe import initialiseer_bord, print_bord, controleer_horizontaal, controleer_winnaar, \
    zet


def tic_tac_toe():
    bord = initialiseer_bord()
    huidige_speler = 'X'
    winnaar = " "
    teller = 0
    einde_spel = False
    while not einde_spel:
        print_bord(bord)

        rij = int(input("Doe een zet "))
        kolom = int(input("DOE een zet in een kolom"))

        bord = zet(bord, rij, kolom, huidige_speler)

        if controleer_winnaar(bord) == True:
            print(f"{huidige_speler} heeft gewonnen")
            return


        if huidige_speler == "X":
            huidige_speler = "0"
        else:huidige_speler = "X"


tic_tac_toe()