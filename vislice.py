import random

def pozdrav():
    print("\n \nDobrodošel v vislicah. Si pripravljen, da obvisiš?")
    print('(1) Da, želim začeti z igro. \n(2) Ne, nočem več igrati.')
    uporabnikova_izbira = input('')
    if uporabnikova_izbira == '1':
        print('Igra se začenja. Napiši črko in pritisni enter. Uporabljaj samo male tiskane črke iz slovenske abecede.')
        zacetek_igre()
    elif uporabnikova_izbira == '2':
        print("Igra se zapira. Adijo!")
        exit()
    else:
        print('Za začetek igre pritisni 1, za izhod pa 2.')
        pozdrav()

def zacetek_igre():
    stevilo_poskusov = 0
    uporabljene_crke = ''
    besede = open("celkupbesed.txt").read().split()
    beseda = random.choice(besede)
    trenutno_stanje = '-' * len(beseda)

    while stevilo_poskusov < 6:
        if trenutno_stanje == beseda:
            zmagovalne_poteze = int(len(uporabljene_crke) / 3)
            print(' \n ČESTITKE, uspelo ti je zmagati v ' + str(zmagovalne_poteze) + ' poskusih.')
            print('Tokrat si preživel... \n \n ')
            pozdrav()

        poskus = input('Napiši črko ->')

        if poskus in beseda and  poskus not in uporabljene_crke:
            print('\nČestitam, tvoja črka se nahaja v iskani besedi.\n')
            uporabljene_crke +=  poskus +', '
            hangman_graphic(stevilo_poskusov, beseda)
            new = ""
            for i in range(len(beseda)):
                if poskus == beseda[i]:
                    new += poskus
                else:
                    new += trenutno_stanje[i]
            trenutno_stanje = new
            print("Napredek: " + trenutno_stanje)
            print('Črke, ki si jih že uporabil:' + uporabljene_crke + '\n \n')

        elif poskus not in beseda and poskus not in uporabljene_crke:
            stevilo_poskusov += 1
            print("NAROBE! V abecedi je 25 črk in ti si izbral ravno to?! \n ")
            uporabljene_crke += poskus +', '
            hangman_graphic(stevilo_poskusov, beseda)
            print("Napredek: " + trenutno_stanje)
            print("Črke, ki si jih že uporabil: " + uporabljene_crke + '\n \n')
        else:
            print('To črko si že uporabil. Poskusi še enkrat.')


def hangman_graphic(stevilo_poskusov, beseda):
    if stevilo_poskusov == 0:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif stevilo_poskusov == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif stevilo_poskusov == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif stevilo_poskusov == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif stevilo_poskusov == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif stevilo_poskusov == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    else:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        print("Ohjoj! Obvisel si - IGRE ŽIVLJENJA JE KONEC!")
        print('Beseda, ki si jo iskal je: ' + beseda + '. \n \n \n')
        pozdrav()

