# -*-coding: utf-8 -*-
__authors__ = 'grousselle', 'dbukhartsev'
# $server = "localhost";
# $user = "grousselle";
# $password = "grousselledf23";
# $base = "grousselle";
import MySQLdb


def RemoveLogin(login):

    try :
        # ouverture de base sql (serveur,user,mdp,base)
        db = MySQLdb.connect("localhost", "grousselle", "grousselledf23", "grousselle")
        bd_cursor = db.cursor()
        sqlCommand = "SELECT * from etudiants"
        print sqlCommand
        sqlCommand2 = "delete from etudiants where LOGIN='" + login + "'"
        print sqlCommand2
        bd_cursor.execute(sqlCommand2)
        db.close()
    except Exception:
        return 1

a = raw_input("réntrer le login de la personne a supprimer ")
b = RemoveLogin(a)
print b
if (b == 1):
    print ("une erreur lors de la suppression")
else:
    print ("le compte est supprimé")
# nous pouvons egalement gerer la suppression par année en ajoutant une condition redoublement ou non
