import numpy as np
import tkinter as tk
from tkinter import messagebox

'''
Fonction initialisant le message à coder: le demande à l'utilisateur puis le normalise
'''
def initialisation(message=None):
    if message is None:
        raise ValueError("Un message doit être fourni pour l'initialisation.")
    print(f"[DEBUG] Message avant normalisation : {message}")
    message = message.replace('é', "e")
    message = message.replace('è', "e")
    message = message.upper()
    message = message.replace(' ', '')
    message = message.replace("'", "")
    print(f"[DEBUG] Message après normalisation : {message}")
    return message

'''
Transforme le message en une chaîne numérique en soustrayant la valeur min des ASCII pour le normaliser
'''
def num(message):
    string = [ord(char) - 64 for char in message]
    print(f"[DEBUG] Message converti en valeurs numériques : {string}")
    return string

'''
Génère la clef à utiliser, boucle sur la taille du message pour générer une clef de la bonne longueur
'''
def genererClef(liste, taille):
    """
    Génère une clé en modifiant la pile de cartes existante.
    """
    global clef
    clef.clear()  
    for _ in range(taille):
        liste = etape1(liste) 
        liste = lecturecartes(liste)  
    print(f"[DEBUG] Nouvelle clé générée : {clef}")
    return liste 

'''
Fonction correspondant à la phase de lecture des cartes et à leur manipulation
'''
def lecturecartes(liste):
    liste=etape2(liste)
    liste=etape3(liste)
    liste=etape4(liste)
    return liste

'''
Fonction cryptant le message à partir de la clef précédemment générée et mise en paramètre
'''
def crypter(message, clef):
    print(f"[DEBUG] Message à crypter (numérique) : {message}")
    print(f"[DEBUG] Clé utilisée pour le cryptage : {clef}")
    inte = [(m + c) % 26 for m, c in zip(message, clef)]
    string = [chr(c + 64) for c in inte]
    print(f"[DEBUG] Message crypté : {string}")
    return string

'''
Fonction décryptant le message à partir de la clef
'''
def decrypter(code, clef):
    print(f"[DEBUG] Message crypté (entrée) : {code}")
    print(f"[DEBUG] Clé utilisée pour le décryptage : {clef}")
    # On convertit le message crypté en indices numériques
    code = [ord(char) - 64 for char in code]
    inte = [((co - cl + 26) % 26) for co, cl in zip(code, clef)]
    string = [chr(c + 64) if c != 0 else 'Z' for c in inte]
    print(f"[DEBUG] Message décrypté (numérique) : {inte}")
    print(f"[DEBUG] Message décrypté (texte) : {''.join(string)}")
    return ''.join(string)

'''
Etape de la manipulation des jokers 
'''
def etape1(liste):
    print(f"[DEBUG] Liste avant étape 1 : {liste}")
    position_n = np.where(liste == JOKER_NOIR)[0][0]
    position_r = np.where(liste == JOKER_ROUGE)[0][0]
    if position_n == 53:
        np.delete(liste,53)
        np.insert(liste,1,JOKER_NOIR)
    else:
        np.delete(liste,position_n)
        np.insert(liste,position_r-1,JOKER_NOIR)
    if position_r == 53:
        np.delete(liste,53)
        np.insert(liste,2,JOKER_ROUGE)
    elif position_r == 52:
        np.delete(liste,52)
        np.insert(liste,1,JOKER_ROUGE)
    else:
        np.delete(liste,position_r)
        np.insert(liste,position_r-2,JOKER_ROUGE)
    print(f"[DEBUG] Liste après étape 1 : {liste}")
    return liste

'''
Etape du découpage du paquet en trois selon la position des jokers dans le paquet
'''
def etape2(liste):
    print(f"[DEBUG] Liste avant étape 2 : {liste}")
    position_n = np.where(liste == JOKER_NOIR)[0][0]
    position_r = np.where(liste == JOKER_ROUGE)[0][0]
    if position_n > position_r:
        liste=np.concatenate([liste[position_n+1:],liste[position_r:position_n+1],liste[:position_r]])
    else :
        liste=np.concatenate([liste[position_r+1:],liste[position_n:position_r+1],liste[:position_n]])
    print(f"[DEBUG] Liste après étape 2 : {liste}")
    return liste

'''
Etape remontant les cartes indiquées par la dernière carte
'''
def etape3(liste):
    print(f"[DEBUG] Liste avant étape 3 : {liste}")
    n = liste[-1]
    if n != (53 | 54): 
        liste = np.concatenate([liste[n:-1],liste[:n],liste[-1:]])
    print(f"[DEBUG] Liste après étape 3 : {liste}")
    return liste

'''
Détermination de la clef selon la position indiquée par la première carte
'''
def etape4(liste):
    print(f"[DEBUG] Liste avant étape 4 : {liste}")
    n = liste[0]
    if n==54:
        n=53
    m = liste[n]
    if m == (53 | 54):
        etape2(liste)
    else:
        m = m % 26
        clef.append(m)
    print(f"[DEBUG] Liste après étape 4 : {liste}")
    return liste


'''
On garde le tas initial pour le transmettre à notre correspondant
'''
np.random.seed()
liste=np.random.permutation(np.arange(1,55))

liste_initiale=liste
clef=[]
JOKER_NOIR = 53
JOKER_ROUGE = 54
