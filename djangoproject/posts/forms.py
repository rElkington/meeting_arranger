from django import forms
from .models import meeting, staff_users

#widgets let you format the html for the field
#forms.ChoiceField lets you do drop down menu
#shite most of this stuff only works in chrome

class HomeForm(forms.ModelForm):
    lect_name = forms.ModelChoiceField(label='Lecturer name', queryset=staff_users.objects.all()) #is it better with widget=forms.TextInput(attrs={"placeholder": "Lecturer name"})
    m_date = forms.DateField(label='Meeting date', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    m_time = forms.TimeField(label='Time', widget=forms.widgets.DateInput(attrs={'type': 'time', 'placeholder':'Select a date'}))
    descript = forms.CharField(label='Meeting description') # is this better with widget=forms.Textarea() - QUALATATIVE DISCUSSION FOR REPORT: should this be required (realistically yes because otherwise lecturers likely to not know whats up)

    class Meta:
        model = meeting
        fields = ('lect_name', 'm_date', 'm_time', 'descript')
