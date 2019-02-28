from django import forms
from .models import NewCarModel


class NewCarForm(forms.ModelForm):
    class Meta():
        model = NewCarModel
        fields = '__all__'

    def clean_year(self):
        yearData = self.cleaned_data['year']

        if yearData < 2019:
            raise forms.ValidationError('that is not a new car.')

        return yearData

    def clean_mpg(self):
        mpgData = self.cleaned_data['mpg']


        if mpgData < 20:
            raise forms.ValidationError("that's to low!!")


        if mpgData > 500:
            raise forms.ValidationError("that's Impossible.")

        return mpgData