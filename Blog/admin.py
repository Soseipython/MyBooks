from django.contrib import admin
from Blog import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "publisher", "theme",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birthYear", "deathYear",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(models.Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}