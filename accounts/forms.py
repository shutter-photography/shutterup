from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class Customercreateform(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'DISPLAY NAME'
        self.fields['email'].label = 'EMAIL-ID'
        self.fields['password1'].label = 'PASSWORD'
        self.fields['password2'].labels = 'CONFIRM PASSWORD'
