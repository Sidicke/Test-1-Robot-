from ClassRobot import Robot
class RobotMedical(Robot):
    """
    Robot spécialisé dans les tâches médicales
    Ex: Robot chirurgien, robot de désinfection, etc.
    """
    
    def __init__(self, *args, type_operation, sterilisable, telecommande,
                 compatibilite_scan, precision_chirurgicale):
        """
        Initialise un robot médical
        
        Args:
            type_operation (str): Type d'opération médicale réalisée
            sterilisable (bool): Possibilité de stérilisation complète
            telecommande (bool): Contrôle à distance possible
            compatibilite_scan (str): Compatibilité avec les systèmes d'imagerie
            precision_chirurgicale (str): Précision des gestes en microns
        """
        super().__init__(*args)
        self.type_operation = type_operation
        self.sterilisable = sterilisable
        self.telecommande = telecommande
        self.compatibilite_scan = compatibilite_scan
        self.precision_chirurgicale = precision_chirurgicale

    def move(self):
        """Déplacement spécifique pour un robot médical"""
        print(f"{self.get_nom()} se positionne pour une intervention chirurgicale.")

    def get_type(self):
        """Retourne le type de robot"""
        return "RobotMedical"

    def get_attributs_specifiques(self):
        """Retourne les attributs spécifiques au robot médical"""
        return {
            "type_operation": self.type_operation,
            "sterilisable": self.sterilisable,
            "telecommande": self.telecommande,
            "compatibilite_scan": self.compatibilite_scan,
            "precision_chirurgicale": self.precision_chirurgicale
        }

