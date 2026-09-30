from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']
    