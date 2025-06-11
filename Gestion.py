
def demander_attributs(generaux, specifiques):
    """
    Demande à l'utilisateur de saisir les valeurs pour chaque attribut
    
    Args:
        generaux (list): Liste des noms des attributs généraux
        specifiques (list): Liste des noms des attributs spécifiques
        
    Returns:
        list: Liste des valeurs saisies par l'utilisateur
    """
    reponses = []
    
    print("\n--- Entrez les attributs généraux ---")
    for attr in generaux:
        # On saute l'ID qui est généré automatiquement
        if attr == "id_robot":
            continue
            
        # Validation spécifique pour certains champs
        if attr == "annee_fabrication":
            while True:
                try:
                    val = int(input(f"{attr} (année entre 2000 et 2025) : "))
                    if 2000 <= val <= 2025:
                        reponses.append(str(val))
                        break
                    else:
                        print("L'année doit être entre 2000 et 2025")
                except ValueError:
                    print("Veuillez entrer un nombre valide")
        elif attr == "vitesse_max" or attr == "poids":
            while True:
                try:
                    val = float(input(f"{attr} (nombre positif) : "))
                    if val > 0:
                        reponses.append(str(val))
                        break
                    else:
                        print("La valeur doit être positive")
                except ValueError:
                    print("Veuillez entrer un nombre valide")
        elif attr == "statut":
            while True:
                val = input(f"{attr} (En service/En maintenance/Hors service) : ").strip()
                if val in ["En service", "En maintenance", "Hors service"]:
                    reponses.append(val)
                    break
                else:
                    print("Statut invalide. Choisissez parmi: En service, En maintenance, Hors service")
        else:
            val = input(f"{attr} : ").strip()
            while not val:  # Validation que le champ n'est pas vide
                print("Ce champ ne peut pas être vide")
                val = input(f"{attr} : ").strip()
            reponses.append(val)
    
    print("\n--- Entrez les attributs spécifiques ---")
    for attr in specifiques:
        # Validation pour les booléens
        if attr in ["detergent", "sterilisable", "telecommande", 
                   "compatibilite_scan", "interaction_voix", 
                   "apprentissage", "reconnaissance_visage"]:
            while True:
                val = input(f"{attr} (oui/non) : ").lower().strip()
                if val in ["oui", "non"]:
                    reponses.append(val == "oui")
                    break
                else:
                    print("Veuillez répondre par 'oui' ou 'non'")
        else:
            val = input(f"{attr} : ").strip()
            while not val:  # Validation que le champ n'est pas vide
                print("Ce champ ne peut pas être vide")
                val = input(f"{attr} : ").strip()
            reponses.append(val)
    
    return reponses


def sauvegarder_robots(robots):
    """
    Sauvegarde la liste des robots dans un fichier texte
    
    Args:
        robots (list): Liste des objets Robot à sauvegarder
    """
    with open("robots_crees.txt", "w", encoding="utf-8") as f:
        for robot in robots:
            f.write(f"=== {robot.get_type()} ===\n")
            for cle, val in robot.get_attributs_generaux().items():
                f.write(f"{cle} : {val}\n")
            for cle, val in robot.get_attributs_specifiques().items():
                f.write(f"{cle} : {val}\n")
            f.write("\n")


def afficher_menu():
    """Affiche le menu principal avec les types de robots disponibles"""
    print("\n=== Types de robots disponibles ===")
    print("1. Robot Ménager - Pour les tâches domestiques (nettoyage, etc.)")
    print("2. Robot Industriel - Pour les usines et chaînes de production")
    print("3. Robot Médical - Pour les interventions chirurgicales")
    print("4. Robot Explorateur - Pour l'exploration de milieux difficiles")
    print("5. Robot Compagnon - Pour l'assistance et la compagnie")
    print("6. Quitter le programme")