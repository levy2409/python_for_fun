import random
import csv
data_base = "data_base.csv"

def nombre():
    nom_user = input("Entrez votre nom : ")
    nombre_aleatoire = random.randint(1, 1000)
    print(nombre_aleatoire)
    tentative = 0
    a = True
    while(a):
        chiffre_saisi = int(input("Entrez un chiffre : "))
        if chiffre_saisi == nombre_aleatoire:
            a = False
        elif chiffre_saisi < nombre_aleatoire:
            print('chiffre plus grand')
            tentative = tentative + 1
        else:
            print('chiffre plus petit')
            tentative = tentative + 1
    # print(tentative)
    print(f'Bravo {nom_user} gagnere au bout de {tentative}')
    with open(data_base, mode='a', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom_user, tentative])

def affichage_user():
    with open(data_base, mode='r', encoding='utf-8') as fichier:
        reader = csv.reader(fichier)
        lignes = list(reader)
        
        lignes_triees = sorted(lignes, key=lambda ligne: int(ligne[1]))

        for ligne in lignes_triees:
            print(ligne)  # Affiche la ligne sous forme de liste


menu_bol = True
while menu_bol:
    menu = int(input("Que voulais vous faire \n1 Jouer \n2 afficher les joueurs\n3 exit : "))
    if menu == 1:
        nombre()
    elif menu == 2:
        affichage_user()
    else:
        menu_bol =False