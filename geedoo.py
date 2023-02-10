# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def OuExclusif(valeur1, valeur2):
    resultat= ""
    tableauK = ["" for i in range(len(valeur1))]
    for i in range(len(valeur1)):
        val1 = valeur1[i:i + 1]
        val2 = valeur2[i:i + 1]

        tableauK[i] = "0" if val1 == val2 else "1"

    for i in tableauK:
        resultat+= i
    return resultat


def OuLogique(valeur1, valeur2):
    resultat= ""
    tableauK = ["" for i in range(len(valeur1))]
    for i in range(len(valeur1)):
        val1 = valeur1[i:i + 1]
        val2 = valeur2[i:i + 1]

        tableauK[i] = "1" if val1 == "1" or val2 == "1" else "0"

    for i in tableauK:
        resultat+= i
    return resultat


def ETlogique(valeur1, valeur2):
    resultat= ""
    tableauK = [""] * len(valeur1)
    for i in range(len(valeur1)):
        val1 = valeur1[i:i + 1]
        val2 = valeur2[i:i + 1]
        tableauK[i] = "1" if val1 == "1" and val2 == "1" else "0"
    resultat= "".join(tableauK)
    return resultat



def permut(valeur, k):
    resultat= ""
    tableauK = [0] * len(valeur)

    for i in range(len(valeur)):
        id = k[i:i + 1]
        vid = int(id)
        tableauK[i] = valeur[vid]
        resultat+= tableauK[i]

    return resultat


def inverse_permut(k):
    resultat= ""
    tableauK = [0] * len(k)

    for i in range(len(k)):
        id = k[i:i + 1]
        vid = int(id)
        tableauK[vid] = str(i)

    resultat= ''.join(tableauK)

    return resultat


def decalage(valeur, ordre, gauche):
    resultat= ""
    tableauK = [""] * len(valeur)
    s = -1 if gauche else 1
    for i in range(len(valeur)):
        valeur1 = valeur[i:i + 1]
        o = ordre
        j = i
        while o > 0:
            if j + s < 0:
                j = len(valeur) - 1
            elif j + s >= len(valeur):
                j = 0
            else:
                j = j + s
            o -= 1
        tableauK[j] = valeur1
    resultat= "".join(tableauK)
    return resultat



def generateKey(k, pk, gdecalage, ddecalage):
    resultat= ""
    nk = permut(k, pk)
    k1 = nk[0:4]
    k2 = nk[4:8]
    nk1 = OuExclusif(k1, k2)
    nk2 = ETlogique(k1, k2)
    dnk1 = decalage(nk1, gdecalage, True)
    dnk2 = decalage(nk2, ddecalage, False)
    resultat= dnk1 + "," + dnk2
    #print("resultatkeygen " + res)
    return resultat

def roundDChiffre(valeur, kp, k):
    resultat= ""
    perm = permut(valeur, kp)
    resultat= OuExclusif(perm, k)
    return resultat


def roundGChiffre(valeurd, valeurg, k):
    resultat= ""
    fc = OuLogique(valeurg, k)
    resultat= OuExclusif(valeurd, fc)
    return resultat

def roundGDechiffre(valeur, kp, k):
    resultat= ""
    nkp = inverse_permut(kp)
    c = OuExclusif(valeur, k)
    resultat= permut(c, nkp)
    return resultat


def roundDDechiffre(valeurd, valeurg, k):
    resultat= ""
    fc = OuLogique(valeurg, k)
    resultat= OuExclusif(valeurd, fc)
    return resultat



def main():


    print("*********************************************************************")
    print("********TRAVAIL PRATIQUE SUR L'ALGORITHME DE FREISNEL CIPHER*********")
    print("*********************************************************************")

    print("Veillez entrer une clé K de longueur 8")
    key = input()

    while len(key) < 8:
        print("La taille de la clé k doit être de longueur 8")
        key = input()
    print("Veillez donner la fonction H de permutation")
    h = input()


    while len(h) < 8:
        print("La taille de la fonction H doit être de longueur 8")
        h = input()
        decg = 0
        decd = 0
        print("Veillez entrer l'ordre de décalage à gauche")
        decg = int(input())


    while decg <= 0:
        print("L'ordre doit être supérieur à 0")
        decg = int(input())
        print("Veillez entrer l'ordre de décalage à droite")
        decd = int(input())

    while decd <= 0:
        print("L'ordre doit être supérieur à 0")
        decd = int(input())
        kgen = generateKey(key, h, decg, decd)
        print("Veillez entrer la valeur N ou C à traiter")
        n = input()
        
    while len(n) < 8:
        print("La taille doit être de longueur 8")
        n = input()
        choix = -1

    while choix != 1 and choix != 2:
        print("Voulez-vous chiffrer ou dechiffrer? (1 pour dechiffrer et 2 pour chiffrer)")
        choix = int(input())
        print("Veillez entrer la permutation P de 4 bits")
        p = input()

    while len(p) < 4:
        print("La taille doit être de longueur 4")
        p = input()
        print("Veillez entrer la clé de permutation pour l'opération de chiffrement ou déchiffrement")
        keyc = input()


    while len(keyc) < 8:
        print("La taille doit être de longueur 8")
        keyc = input()
        tkey = kgen.split(",")


    if choix == 2:
        pn = permut(n, keyc)
        g0 = pn[:4]
        d0 = pn[4:8]
        d1 = roundDChiffre(g0, p, tkey[0])
        g1 = roundGChiffre(d0, g0, tkey[0])
        d2 = roundDChiffre(g1, p, tkey[1])
        g2 = roundGChiffre(d1, g1, tkey[1])
        c = g2 + d2
        ikey = inverse_permut(keyc)
        resultat= permut(c, ikey)
        print("***********************************")
        print("La valeur chiffrée est :", resultat)
        print("***********************************")

    else:
        pn = permut(n, keyc)
        g2 = pn[:4]
        d2 = pn[4:8]
        g1 = roundGDechiffre(d2, p, tkey[1])
        d1 = roundDDechiffre(g2, g1, tkey[1])
        g0 = roundGDechiffre(d1, p, tkey[0])
        d0 = roundDDechiffre(g1, g0, tkey[0])
        Nd = g0 + d0
        ikey = inverse_permut(keyc)
        resultat= permut(Nd, ikey)
        print("***********************************")
        print("La valeur déchiffrée est :", resultat)
        print("***********************************")
main()
#test value to enter k 01101101 h 65274130 n 01101110 hh 46027315 P 2013 C : 10110010

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
