import hashlib

def valider_password(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    symbols = "!@#$%^&*"

    # Vérification de la longueur du mot de passe
    if len(password) < 8:
        print("Il doit contenir au moins 8 caractères.")
        return False
    
    #Vérifier les caractères:
    for character in password:
        if character.isupper():
            has_upper =True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif character in symbols():
            has_symbol = True
    
    if not has_upper:
        print ("Il doit contenir au moins une lettre majuscule.")
    if not has_lower:
        print("il doit contenir au moins une lettre minuscule.")
    if not has_digit:
        print ("il doit contenir au moins un chiffre.")
    if not has_symbol:
        print("Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")


        if has_lower and has_upper and has_digit and has_symbol:
            print("Le mot de passe est valide !")
            return True
        else:
            return False
password =input("Veuillez ecrire votre mots de passe: ")
print(password)
valider_password(password)

hash_mdp = hashlib.sha256() # Créer un objet de hachage SHA-256
hash_mdp.update(password.encode()) # Encoder le mot de passe en bytes et le passer à l'algorithme de hachage
mot_de_passe_hache = hash_mdp.hexdigest() # Obtenir le mot de passe haché (en hexadécimal)
print("Votre mot de passe haché est :", mot_de_passe_hache)