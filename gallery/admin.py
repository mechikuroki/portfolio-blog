from django.contrib import admin
from .models import Product, Comment, Tag

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Tag)
