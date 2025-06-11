"""
Programme de gestion de robots avec différentes spécialisations
Permet de créer, afficher et sauvegarder des robots de différents types
"""

from abc import ABC, abstractmethod
import uuid  # Pour générer des IDs uniques automatiquement

class Robot(ABC):
    """
    Classe abstraite de base pour tous les types de robots
    Contient les attributs communs à tous les robots
    """
    
    def __init__(self, nom, fabricant, modele, annee_fabrication,
                 batterie, capacite_charge, vitesse_max, poids, statut):
        """
        Initialise un robot avec ses attributs généraux
        
        Args:
            nom (str): Nom donné au robot
            fabricant (str): Nom du fabricant du robot
            modele (str): Modèle du robot
            annee_fabrication (int): Année de fabrication du robot
            batterie (str): Type de batterie (Li-ion, NiMH, etc.)
            capacite_charge (str): Capacité de charge en Ah (ampère-heure)
            vitesse_max (float): Vitesse maximale en km/h
            poids (float): Poids en kg
            statut (str): Statut actuel (En service, En maintenance, Hors service)
        """
        self._id_robot = str(uuid.uuid4())[:8]  # Génère un ID unique de 8 caractères
        self._nom = nom
        self._fabricant = fabricant
        self._modele = modele
        self._annee_fabrication = annee_fabrication
        self._batterie = batterie
        self._capacite_charge = capacite_charge
        self._vitesse_max = vitesse_max
        self._poids = poids
        self._statut = statut

    def get_nom(self):
        """Retourne le nom du robot"""
        return self._nom

    def get_attributs_generaux(self):
        """Retourne un dictionnaire avec tous les attributs généraux"""
        return {
            "nom": self._nom,
            "id_robot": self._id_robot,
            "fabricant": self._fabricant,
            "modele": self._modele,
            "annee_fabrication": self._annee_fabrication,
            "batterie": self._batterie,
            "capacite_charge": self._capacite_charge,
            "vitesse_max": self._vitesse_max,
            "poids": self._poids,
            "statut": self._statut,
        }

    @abstractmethod
    def move(self):
        """Méthode abstraite - Définit comment le robot se déplace"""
        pass

    @abstractmethod
    def get_type(self):
        """Méthode abstraite - Retourne le type du robot"""
        pass

    @abstractmethod
    def get_attributs_specifiques(self):
        """Méthode abstraite - Retourne les attributs spécifiques au type de robot"""
        pass








