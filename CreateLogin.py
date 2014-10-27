# -*- coding: utf-8 -*-
__authors__ = 'grousselle', 'dbukhartsev'
import random
import MySQLdb


def CreateLogin(Nom, Prenom):
    # prend la 1ere lettre du prenon et les 7 premiere lettres du nom
    login1 = Prenom[0] + Nom[0:7]
    # nous allons maintenant enlever les -
    login = login1.lower().replace("-", "")
    print ("votre login " + login + " a ete creer")
    return login


def CreateMDP():
    MDP = []
    liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cpt = 0
    while (cpt < 8):
        chiffre = random.randint(1, 60)
        # print chiffre # debug pour savoir si les chiffres sont bien genere
        # creer le mot de passe sous la forme d'une liste creer a base de generation aleatoire
        MDP.append(liste[chiffre])
        #print MDP # debug affiche la liste des element composant le mot de passe
        cpt = cpt + 1
    c = ''
    mdp = c.join(MDP)
    # print mdp
    return mdp


def ajoutBD(login, mdp, annee):
    try:
        # base de données accessible depuis SSH KHEOPS
        db = MySQLdb.connect("localhost", "grousselle", "grousselledf23", "grousselle")
        bd_cursor = db.cursor()
        sqlCommand = "INSERT INTO etudiants (LOGIN, PASSWD, YEAR) VALUES ('" + login + "', '" + mdp + "', '" + annee + "')"
        # print sqlCommand sert a verifier si on ajoute les bonnes variables
        bd_cursor.execute(sqlCommand)
        db.close()
    except Exception:
        return 1


a = raw_input("Veuillez entrer votre Nom :")
b = raw_input("Veuillez entrer votre Prenom :")
c = raw_input("Annee  :")
mdp = CreateMDP()
login = CreateLogin(a, b)
print "Et son mdp est " + mdp
d = ajoutBD(login, mdp, c)
if (d == 1):
    print ("une erreur lors de l'ajout a ete detecte")
else:
    print ("Ajoute effectué")
