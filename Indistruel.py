from ClassRobot import Robot
class RobotIndustriel(Robot):
    """
    Robot spécialisé dans les tâches industrielles
    Ex: Robot sur chaîne de montage, robot soudeur, etc.
    """
    
    def __init__(self, *args, type_usine, outil_utilise, resistance_chaleur,
                 capacite_production, precision):
        """
        Initialise un robot industriel
        
        Args:
            type_usine (str): Type d'usine où le robot est utilisé
            outil_utilise (str): Outil principal utilisé par le robot
            resistance_chaleur (str): Résistance à la chaleur en °C
            capacite_production (str): Capacité de production (unités/heure)
            precision (str): Précision des opérations en mm
        """
        super().__init__(*args)
        self.type_usine = type_usine
        self.outil_utilise = outil_utilise
        self.resistance_chaleur = resistance_chaleur
        self.capacite_production = capacite_production
        self.precision = precision

    def move(self):
        """Déplacement spécifique pour un robot industriel"""
        print(f"{self.get_nom()} se déplace sur la chaîne de production.")

    def get_type(self):
        """Retourne le type de robot"""
        return "RobotIndustriel"

    def get_attributs_specifiques(self):
        """Retourne les attributs spécifiques au robot industriel"""
        return {
            "type_usine": self.type_usine,
            "outil_utilise": self.outil_utilise,
            "resistance_chaleur": self.resistance_chaleur,
            "capacite_production": self.capacite_production,
            "precision": self.precision
        }
