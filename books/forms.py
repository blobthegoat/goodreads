from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Rating
from django.forms import ModelForm

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']

class ReviewForm(ModelForm):
    class Meta():
        model = Rating
        fields = ['score', 'body']
    