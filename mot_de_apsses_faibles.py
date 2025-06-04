import random

mots_de_passe_faibles = [
    "123456", "password", "admin", "123456789", "qwerty",
    "abc123", "letmein", "welcome", "monkey", "football"
]

mot_secret = random.choice(mots_de_passe_faibles)

tentatives = []

max_essais = int(input("Nombre maximum d’essais autorisés : "))

triche = input("Activer l’option triche ? (oui/non) : ").lower()
if triche == "oui":
    print(f"[Triche] Le mot de passe est : {mot_secret}")

trouve = False
compteur = 0

while not trouve and compteur < max_essais:
    guess = input("Devinez le mot de passe : ")
    tentatives.append(guess)
    compteur += 1

    if guess == mot_secret:
        print(f"Bravo ! Mot de passe trouvé en {compteur} essai(s).")
        trouve = True
    else:
        print("Incorrect.")
        
        if len(guess) > len(mot_secret):
            print("Indice : Le mot de passe est plus court.")
        elif len(guess) < len(mot_secret):
            print("Indice : Le mot de passe est plus long.")
        
        if guess and mot_secret and guess[0] == mot_secret[0]:
            print("Indice : Le mot de passe commence par la même lettre.")
        
        lettres_communes = sum(1 for c in set(guess) if c in mot_secret)
        print(f"Indice : {lettres_communes} lettre(s) en commun.")

if not trouve:
    print(f"Échec. Le mot de passe était : {mot_secret}")

print("\nHistorique des tentatives :")
for i, essai in enumerate(tentatives, 1):
    print(f"{i}. {essai}")
