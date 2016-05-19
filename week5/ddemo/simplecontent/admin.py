from django.contrib import admin
from .models import Article, Comment, Photo, Power, SuperHero, SuperHeroPower

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(Power)
admin.site.register(SuperHero)
admin.site.register(SuperHeroPower)
