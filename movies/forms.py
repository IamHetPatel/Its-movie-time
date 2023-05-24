from django import forms

class BookingForm(forms.Form):
    date = forms.DateField()
    num_tickets = forms.IntegerField(min_value=1)
