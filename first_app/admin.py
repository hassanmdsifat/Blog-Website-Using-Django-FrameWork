from django.contrib import admin
from .models import Catagory,Post,Comment
from django import forms
# Register your models here.

admin.site.register(Catagory)

admin.site.register(Comment)
class add_editor(forms.ModelForm):
    class Meta:
        model=Post
        widgets = {
            "Body":forms.Textarea,
        }
        fields='__all__'
    
class AddEditor(admin.ModelAdmin):
    form=add_editor
    list_display=("PostId","Title","Catagory")


admin.site.register(Post,AddEditor)