from ClassRobot import Robot
from Menage import RobotMenager
from Indistruel import RobotIndustriel 
from Medical import RobotMedical
from Explorateur import RobotExplorateur
from Compagnon import RobotCompagnon
from Gestion import demander_attributs,sauvegarder_robots,afficher_menu
def main():
    """Fonction principale du programme"""
    
    # Liste des attributs généraux (sans id_robot qui est généré automatiquement)
    generaux = ["nom", "fabricant", "modele", "annee_fabrication",
                "batterie", "capacite_charge", "vitesse_max", "poids", "statut"]

    # Dictionnaire des classes de robots disponibles
    robot_classes = {
        "1": ("RobotMénager", RobotMenager, ["type_tache", "reservoir", "detergent", "autonomie", "niveau_bruit"]),
        "2": ("RobotIndustriel", RobotIndustriel, ["type_usine", "outil_utilise", "resistance_chaleur", "capacite_production", "precision"]),
        "3": ("RobotMedical", RobotMedical, ["type_operation", "sterilisable", "telecommande", "compatibilite_scan", "precision_chirurgicale"]),
        "4": ("RobotExplorateur", RobotExplorateur, ["type_exploration", "profondeur_max", "communication", "resistance", "capacite_analyse"]),
        "5": ("RobotCompagnon", RobotCompagnon, ["intelligence_sociale", "interaction_voix", "apprentissage", "reconnaissance_visage", "divertissement"]),
    }

    robots_crees = []  # Liste pour stocker les robots créés

    print("\n=== Programme de création de robots ===")
    print("Créez et gérez différents types de robots\n")

    while True:
        afficher_menu()
        choix = input("\nChoisissez un type de robot à créer (1-5) ou 6 pour quitter : ").strip()
        
        # Option pour quitter
        if choix == "6":
            if robots_crees:
                sauvegarder_robots(robots_crees)
                print("\nLes robots ont été sauvegardés dans le fichier 'robots_crees.txt'.")
            print("\nFin du programme.")
            break
            
        # Validation du choix
        if choix not in robot_classes:
            print("\nChoix invalide. Veuillez entrer un nombre entre 1 et 6.")
            continue

        nom_robot, classe_robot, specifiques = robot_classes[choix]
        print(f"\n=== Création d'un {nom_robot} ===")
        print("Veuillez entrer les informations demandées:\n")
        
        # Demander les attributs avec validation
        attributs = demander_attributs(generaux, specifiques)

        try:
            # Création du robot avec les attributs fournis
            robot = classe_robot(*attributs[:9], **dict(zip(specifiques, attributs[9:])))
            robots_crees.append(robot)
            print("\n=== Robot créé avec succès ===")
            print(f"ID du robot : {robot.get_attributs_generaux()['id_robot']}")
            print("Démonstration du robot :")
            robot.move()  # Appel de la méthode move pour démontrer le robot
        except Exception as e:
            print(f"\nErreur lors de la création du robot : {e}")
            print("Veuillez recommencer la création.")

        # Demander si l'utilisateur veut créer un autre robot
        encore = input("\nVoulez-vous créer un autre robot ? (oui/non) : ").lower().strip()
        while encore not in ["oui", "non"]:
            print("Veuillez répondre par 'oui' ou 'non'")
            encore = input("Voulez-vous créer un autre robot ? (oui/non) : ").lower().strip()
            
        if encore == "non":
            if robots_crees:
                sauvegarder_robots(robots_crees)
                print("\nLes robots ont été sauvegardés dans le fichier 'robots_crees.txt'.")
            print("\nFin du programme.")
            break


if __name__ == "__main__":
    main()