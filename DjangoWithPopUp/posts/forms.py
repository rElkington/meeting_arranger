from django import forms
from .models import meeting, CustomUser

class HomeForm(forms.ModelForm):
    lect_name = forms.ModelChoiceField(label='Lecturer name', queryset=CustomUser.objects.filter(is_teacher=True), widget=forms.Select(attrs={'autocomplete':'off'})) #is it better with widget=forms.TextInput(attrs={"placeholder": "Lecturer name"})
    m_date = forms.DateField(label='Meeting date', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    m_time = forms.TimeField(label='Time', widget=forms.widgets.DateInput(attrs={'type': 'time', 'placeholder':'Select a date'}))
    descript = forms.CharField(label='Meeting description') # is this better with widget=forms.Textarea() - QUALATATIVE DISCUSSION FOR REPORT: should this be required (realistically yes because otherwise lecturers likely to not know whats up)

    class Meta:
        model = meeting
        fields = ('lect_name', 'm_date', 'm_time', 'descript',)
