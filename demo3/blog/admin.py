from django.contrib import admin
from .models import Article,Tag,Category,Ads
# Register your models here.
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Ads)