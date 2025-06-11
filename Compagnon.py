from ClassRobot import Robot
class RobotCompagnon(Robot):
    """
    Robot spécialisé dans l'assistance et la compagnie
    Ex: Robot assistant personnel, robot éducatif, etc.
    """
    
    def __init__(self, *args, intelligence_sociale, interaction_voix,
                 apprentissage, reconnaissance_visage, divertissement):
        """
        Initialise un robot compagnon
        
        Args:
            intelligence_sociale (str): Niveau d'intelligence sociale
            interaction_voix (bool): Possibilité d'interaction vocale
            apprentissage (bool): Capacité d'apprentissage automatique
            reconnaissance_visage (bool): Reconnaissance faciale
            divertissement (str): Types de divertissements proposés
        """
        super().__init__(*args)
        self.intelligence_sociale = intelligence_sociale
        self.interaction_voix = interaction_voix
        self.apprentissage = apprentissage
        self.reconnaissance_visage = reconnaissance_visage
        self.divertissement = divertissement

    def move(self):
        """Déplacement spécifique pour un robot compagnon"""
        print(f"{self.get_nom()} suit son utilisateur pour l'assister.")

    def get_type(self):
        """Retourne le type de robot"""
        return "RobotCompagnon"

    def get_attributs_specifiques(self):
        """Retourne les attributs spécifiques au robot compagnon"""
        return {
            "intelligence_sociale": self.intelligence_sociale,
            "interaction_voix": self.interaction_voix,
            "apprentissage": self.apprentissage,
            "reconnaissance_visage": self.reconnaissance_visage,
            "divertissement": self.divertissement
        }
