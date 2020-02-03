from django import forms


class csv_to_json(forms.Form):
    csv_data = forms.Textarea(label='Enter your csv data here')
    json_data = forms.Textarea(label='Your Json Data will appear here')
