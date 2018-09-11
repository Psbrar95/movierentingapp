from django.forms import ModelForm
from .models import Movies

class MoviesForm(ModelForm):
	class Meta:
		model = Movies
		exclude = ['isRented']