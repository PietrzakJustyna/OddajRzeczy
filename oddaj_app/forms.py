from django.contrib.auth.forms import UserChangeForm
from oddaj_app.models import User


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        password = User.password
