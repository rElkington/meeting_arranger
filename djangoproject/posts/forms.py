from django import forms

class HomeForm(forms.Form):
    lect_name = forms.CharField(label='Lecturers name')
    time = forms.CharField(label='Time')
    date = forms.CharField(label='Meeting date')
    descript = forms.CharField(label='Meeting description')