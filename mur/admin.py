from django.contrib import admin
from .models import Pensee

@admin.register(Pensee)
class PenseeAdmin(admin.ModelAdmin):
    list_display = ('contenu', 'auteur', 'date')
    search_fields = ('contenu', 'auteur')
    list_filter = ('date',)
