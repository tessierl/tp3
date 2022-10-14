"""
Programme fait par Lucas Tessier
Groupe 402

"""
import random


boucle_jeu = True


while boucle_jeu:
    niveau = True
    print("Vous êtes un vaillant guerrier prisonnier dans un couloir, à chaque extrémité du couloir il y a une porte. Chacune de ces portes mène à une salle.  Dans chaque salle, il y a un monstre et chaque monstre a un niveau de difficulté qui lui est propre.")
    niveau_vie = 20
    numero_adversaire = 0
    numero_combat = 0
    nombre_victoire = 0
    nombre_defaite = 0
    while niveau:
        force_adversaire = random.randint(1, 5)
        print("Vous tombez face à face avec un adversaire de difficulté :",force_adversaire)
        choix = int(input("Que voulez-vous faire?"))
