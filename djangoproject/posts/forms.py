from django import forms
from .models import PostModel

#widgets let you format the html for the field
#forms.ChoiceField lets you do drop down menu

class HomeForm(forms.Form):
    lect_name = forms.CharField(label='Lecturers name')
    time = forms.TimeField(label='Time')
    date = forms.DateField(label='Meeting date')
    descript = forms.CharField(label='Meeting description')

class PostModelForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ('lect_name', 'date', 'time', 'descript')