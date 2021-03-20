from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

#subclass the UserCreationsForm and UserChangeForm forms so that they use the new CustomUser model

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)