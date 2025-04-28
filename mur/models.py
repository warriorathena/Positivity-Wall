# Module models de Django, qui permet de définir des classes de modèles (tables de la base de données)
from django.db import models

# Classe 'Pensee' qui hérite de 'models.Model' → cela signifie que c'est un modèle de base de données
class Pensee(models.Model):
    # Le champ 'contenu' contient le texte de la pensée, avec un label "Pensée"
    # TextField = zone de texte longue, comme un paragraphe
    contenu = models.TextField("Pensée")

    # Le champ 'auteur' permet de saisir le nom d’un auteur (facultatif grâce à blank=True)
    # CharField = champ de texte court (limité ici à 100 caractères)
    auteur = models.CharField("Auteur", max_length=100, blank=True)

    # Le champ 'date' stocke automatiquement la date et l'heure de création de l'entrée
    # auto_now_add=True = remplit automatiquement ce champ
    date = models.DateTimeField(auto_now_add=True)

    # La méthode __str__ détermine ce qui s'affiche quand on affiche une instance du modèle (ex: dans l'admin)
    # On retourne l’auteur (ou "Anonyme" s'il est vide) suivi des 30 premiers caractères de la pensée
    def __str__(self):
        return f"{self.auteur or 'Anonyme'} - {self.contenu[:30]}"
