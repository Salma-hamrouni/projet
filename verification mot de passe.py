def check_password_strength(password):
    if len(password) < 8:
        return "Mot de passe trop court !"
    if not any(char.isdigit() for char in password):
        return "Ajoutez un chiffre dans votre mot de passe."
    if not any(char.isupper() for char in password):
        return "Ajoutez une majuscule dans votre mot de passe."
    if not any(char.islower() for char in password):
        return "Ajoutez une minuscule dans votre mot de passe."
    if not any(char in "!@#$%^&*()_+" for char in password):
        return "Ajoutez un caractère spécial (!, @, #, etc.)."
    return "Mot de passe sécurisé !"

# Exemple d'utilisation
mot_de_passe = input("Entrez un mot de passe : ")
print(check_password_strength(mot_de_passe))
