# -*- coding: utf-8 -*-
__author__ = 'grousselle'
import re
import urllib2

#fonction permetant de comparer un texte avec une page web
def WebTracking(url, login):
    resultat = []
    url1 = urllib2.urlopen(url)
    web = url1.read()
    NULL = []
    f = open("insultes.txt", "r")
    texte = f.readlines()
    texte = map(lambda s: s.strip(), texte)
    for i in range(0, len(texte)):
        Tracking = re.findall(texte[i], web)
        if Tracking != NULL:
            resultat.append(Tracking)
    if resultat != []:
        print "Des insultes ont été trouvée pour l'utilisateur " + login
    else:
        print login + " est en régle"
    return resultat

# nous pouvons ici charger la liste des login et faire une recherche
# pour CHAQUE login mais, par manque de temps nous n avons pas pu le mettre en place
k = open("LOGIN.txt", "r")
print k
g = k.readlines()
print g
login = map(lambda s: s.strip(), g)
print login
for i in range(0, len(login)):
    a2 = "http://kheops.unice.fr/~" + login[i] + "/ext"
    b = WebTracking(a2, login[i])
