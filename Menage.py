from ClassRobot import Robot
class RobotMenager(Robot):
    """
    Robot spécialisé dans les tâches ménagères
    Ex: Aspirateur robot, robot laveur de vitres, etc.
    """
    
    def __init__(self, *args, type_tache, reservoir, detergent, autonomie, niveau_bruit):
        """
        Initialise un robot ménager
        
        Args:
            type_tache (str): Type de tâche (Nettoyage, Repassage, etc.)
            reservoir (str): Capacité du réservoir (en ml ou L selon le type)
            detergent (bool): Possibilité d'utiliser du détergent
            autonomie (str): Autonomie en heures
            niveau_bruit (str): Niveau de bruit en dB (décibels)
        """
        super().__init__(*args)
        self.type_tache = type_tache
        self.reservoir = reservoir
        self.detergent = detergent
        self.autonomie = autonomie
        self.niveau_bruit = niveau_bruit

    def move(self):
        """Déplacement spécifique pour un robot ménager"""
        print(f"{self.get_nom()} commence à nettoyer la maison.")

    def get_type(self):
        """Retourne le type de robot"""
        return "RobotMénager"

    def get_attributs_specifiques(self):
        """Retourne les attributs spécifiques au robot ménager"""
        return {
            "type_tache": self.type_tache,
            "reservoir": self.reservoir,
            "detergent": self.detergent,
            "autonomie": self.autonomie,
            "niveau_bruit": self.niveau_bruit
        }