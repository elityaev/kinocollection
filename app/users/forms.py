from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from selections.models import Collection


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    def save(self, commit=True):
        user = super().save(commit=commit)
        Collection.objects.create(user=user)
        return user
