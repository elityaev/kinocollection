from django import forms


class RequestForm(forms.Form):
    GENRE_CHOICES = (
        ('боевик', 'boevik'),
        ('детский', 'detskiy'),
        ('драма', 'drama'),
        ('комедия', 'komediya')
    )

    genre = forms.ChoiceField(label='Жанр', choices=GENRE_CHOICES)
    count = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in range(1, 11)], coerce=int
    )
