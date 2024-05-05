import re

def validate_password(password):
    # Vérifier la longueur du mot de passe
    if len(password) < 8:
        return False, "Le mot de passe doit comporter au moins 8 caractères."
    
    # Vérifier s'il contient au moins une lettre minuscule
    if not re.search("[a-z]", password):
        return False, "Le mot de passe doit contenir au moins une lettre minuscule."
    
    # Vérifier s'il contient au moins une lettre majuscule
    if not re.search("[A-Z]", password):
        return False, "Le mot de passe doit contenir au moins une lettre majuscule."
    
    # Vérifier s'il contient au moins un chiffre
    if not re.search("[0-9]", password):
        return False, "Le mot de passe doit contenir au moins un chiffre."
    
    # Vérifier s'il contient au moins un caractère spécial
    if not re.search("[!@#$%^&*()_+{}\":;']+", password):
        return False, "Le mot de passe doit contenir au moins un caractère spécial."

    return True, "Mot de passe valide."