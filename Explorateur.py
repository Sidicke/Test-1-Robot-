from ClassRobot import Robot
class RobotExplorateur(Robot):
    """
    Robot spécialisé dans l'exploration
    Ex: Robot sous-marin, robot spatial, etc.
    """
    
    def __init__(self, *args, type_exploration, profondeur_max, communication,
                 resistance, capacite_analyse):
        """
        Initialise un robot explorateur
        
        Args:
            type_exploration (str): Type d'environnement exploré
            profondeur_max (str): Profondeur maximale en mètres
            communication (str): Type de communication (radio, satellite, etc.)
            resistance (str): Résistance aux conditions extrêmes
            capacite_analyse (str): Capacité d'analyse en temps réel
        """
        super().__init__(*args)
        self.type_exploration = type_exploration
        self.profondeur_max = profondeur_max
        self.communication = communication
        self.resistance = resistance
        self.capacite_analyse = capacite_analyse

    def move(self):
        """Déplacement spécifique pour un robot explorateur"""
        print(f"{self.get_nom()} explore les environs pour collecter des données.")

    def get_type(self):
        """Retourne le type de robot"""
        return "RobotExplorateur"

    def get_attributs_specifiques(self):
        """Retourne les attributs spécifiques au robot explorateur"""
        return {
            "type_exploration": self.type_exploration,
            "profondeur_max": self.profondeur_max,
            "communication": self.communication,
            "resistance": self.resistance,
            "capacite_analyse": self.capacite_analyse
        }


