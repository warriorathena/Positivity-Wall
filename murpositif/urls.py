"""
URL configuration for murpositif project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# On importe les outils nécessaires de Django pour définir les routes (URL)
from django.contrib import admin  # Pour accéder à l'interface d'administration
from django.urls import path, include  # 'path' pour définir des URLs, 'include' pour inclure des sous-urls d'une app
from django.conf import settings
from django.conf.urls.static import static

# Définition de la liste des routes de l'application Django
urlpatterns = [
    # Route vers l'interface d'administration Django, accessible via /admin/
    path('admin/', admin.site.urls),
    
    # Route racine ('') qui redirige vers les URLs définies dans l'application "mur"
    # Cela veut dire que toutes les URLs de l'app "mur" seront accessibles directement depuis la racine du site
    path('', include('mur.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
