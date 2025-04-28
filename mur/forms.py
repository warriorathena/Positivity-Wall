# On importe le module 'forms' de Django, qui permet de créer des formulaires HTML liés à des modèles
from django import forms

# On importe le modèle 'Pensee' défini précédemment pour lier le formulaire à la base de données
from .models import Pensee

# On crée une classe 'PenseeForm' qui hérite de 'forms.ModelForm' → un formulaire directement lié à un modèle
class PenseeForm(forms.ModelForm):
    
    # La classe Meta permet de configurer les options du formulaire
    class Meta:
        # On indique à quel modèle ce formulaire est lié
        model = Pensee
        
        # On précise les champs du modèle à inclure dans le formulaire
        fields = ['contenu', 'auteur']
        
        # On personnalise l'affichage des champs (ex : nombre de lignes, placeholder)
        widgets = {
            # Champ 'contenu' : zone de texte multiligne (3 lignes), avec un texte d'aide
            'contenu': forms.Textarea(attrs={'rows': 3, 'placeholder': "Écris ta pensée positive..."}),
            
            # Champ 'auteur' : champ texte classique avec un texte indicatif
            'auteur': forms.TextInput(attrs={'placeholder': "Ton nom ou celui de l'auteur (facultatif)"}),
        }
