from django import forms
from .models import POST, UPDATE

class NewPostForm(forms.ModelForm):

    class Meta:

        fields = ('Name','new_image',)
        model = POST


class UpdateModelForm(forms.ModelForm):

    class Meta:

        fields = '__all__'
        model = UPDATE
