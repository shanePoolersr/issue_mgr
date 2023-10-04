from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.fields + ("role", "team")
        
        class CustomUserChangeForm(UserChangeForm):
            class meta(UserChangeForm):
                model = CustomUser
                fields = UserChangeForm.fields