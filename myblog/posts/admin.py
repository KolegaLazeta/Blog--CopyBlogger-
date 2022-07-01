from django.contrib import admin
from .models import Post

# PostAdmin klasa nam sluzi da modifikujemo originalnu admin stranicu
class PostAdmin(admin.ModelAdmin):

    # U nastavku imamo neke metode koje nam pruza modul ModelAdmin 

    # list_updated koristimo da  prikazemo zeljene klone modela (tabele)
    list_display = ['title', 'timestamp', 'updated']

    # list_display_link nam dozvoljava da linkujemo odredjenu kolonu
    list_display_link = ['updated']

    # list_editable nam sluzi da izmenimo podatke

    # list_filter nam daje mogucnost filterovanja kolona
    list_filter = ['title', 'updated']

    # search_field nam omogucava da pretrazujemo kolone
    search_fields = ['title', 'content']

    class Meta:
        model = Post

# Registracija modela u adminu
admin.site.register(Post, PostAdmin)