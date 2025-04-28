# On importe 'render' pour afficher un template HTML, et 'redirect' pour rediriger après soumission d’un formulaire
from django.shortcuts import render, redirect

# On importe le modèle Pensee (pour récupérer et enregistrer les pensées)
from .models import Pensee

# On importe le formulaire lié au modèle Pensee
from .forms import PenseeForm

# Définition de la vue principale 'mur_view'
# Cette fonction va gérer l'affichage du mur et la soumission du formulaire
def mur_view(request):
    # On récupère toutes les pensées de la base de données, triées par date décroissante (les plus récentes en premier)
    pensees = Pensee.objects.order_by('-date')

    # On crée une instance du formulaire :
    # - Si on reçoit une requête POST, on remplit le formulaire avec les données soumises
    # - Sinon, on crée un formulaire vide
    form = PenseeForm(request.POST or None)

    # Si le formulaire est soumis (POST) et valide (tous les champs obligatoires remplis correctement)
    if request.method == 'POST' and form.is_valid():
        # On enregistre la nouvelle pensée dans la base de données
        form.save()
        # On redirige l'utilisateur vers la même page pour éviter de renvoyer le formulaire en cas de rafraîchissement
        return redirect('mur')  # 'mur' doit correspondre au nom de l'URL dans urls.py

    # On affiche la page HTML avec le formulaire et la liste des pensées existantes
    return render(request, 'mur/index.html', {
        'form': form,         # le formulaire à afficher
        'pensees': pensees    # la liste des pensées à afficher
    })
