import string
import random

pool = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "sonderzeichen": string.punctuation,
    "zahlen": string.digits
}

print("--- Passwort Generator Setup ---")
anzahl_gross = int(input("Wie viele Großbuchstaben? "))
anzahl_klein = int(input("Wie viele Kleinbuchstaben? "))
anzahl_zahlen = int(input("Wie viele Zahlen? "))
anzahl_sonder = int(input("Wie viele Sonderzeichen? "))
anzahl_passwoerter = int(input("Wie viele Vorschläge möchtest du generieren? "))

print("\nDeine Passwörter:")

for j in range(anzahl_passwoerter):
    zeichen_liste = []

    for i in range(anzahl_gross):
        zeichen_liste.append(random.choice(pool["uppercase"]))
        
    for i in range(anzahl_klein):
        zeichen_liste.append(random.choice(pool["lowercase"]))
        
    for i in range(anzahl_zahlen):
        zeichen_liste.append(random.choice(pool["zahlen"]))
        
    for i in range(anzahl_sonder):
        zeichen_liste.append(random.choice(pool["sonderzeichen"]))

    random.shuffle(zeichen_liste)
    passwort = "".join(zeichen_liste)

    print(f"{j + 1}. Passwort: {passwort}")