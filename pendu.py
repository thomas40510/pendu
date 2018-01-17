import pendu_fonctions as hm
import drawhm as dHM
from firebase import firebase
import os

global size
size = os.get_terminal_size()

def Menu():
    os.system('cls')
    print('*'.center(size.columns, '*'))
    print("Bienvenue dans le jeu du pendu !")
    print("Que voulez-vous faire ?")
    print("\n [1] : jouer \n [2] : leaderboard \n [3] : quitter \n")

    choice = input(">> ")
    while(choice not in ("1","2","3")):
        print("Je n'ai pas bien compris... Merci de répéter")
        choice = input(">> ")

    if choice=="1":
        init()
    elif choice=="2":
        showScores()
    else :
        exit()


def init():
    global mot
    mot = hm.choisir_mot("mots_francais.txt")
    score = 6
    letters=[""]
    os.system('cls')
    play(score,letters)

def showScores():
    os.system('cls')
    mFirebaseApp = firebase.FirebaseApplication("https://pendu-fdc2e.firebaseio.com/", None)
    print('LEADERBOARD'.center(size.columns, '*'))
    leaderboard = mFirebaseApp.get("/users", None)
    for i in range(6,2,-1):
        print("Ont un score de ",i," : ")
        l=[]
        for s in leaderboard:
            if leaderboard.get(s)==i:
                l.append(s+"\n")
        if (l!=[]):
            for c in l:
                print(c)
        else :
            print("None \n")
    print("\n")
    print(' Press any key to continue... '.center(size.columns, '*'))
    input('')

    Menu()

def play(score,letters):
    c = hm.entrer_lettre()
    letters.append(c)
    if (hm.mot_trouve(mot, letters)):
        hm.gameEnd(c,True,mot,score)
        if (hm.askNG()):
            init()
    elif ((c not in mot)):
        score = score-1
        dHM.drawhm(6-score)
        if (score==0):
            hm.gameEnd(c,False,mot,score)
            if (hm.askNG()):
                init()
            else :
                exit()
    print(hm.mot_etoiles(mot, letters))
    play(score,letters)


#if(input("Bienvenue dans le pendu. Une petie partie ? (Y/N) ")=="Y"):
Menu()
