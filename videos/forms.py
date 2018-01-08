from django import forms
from .models import fileDetails, tvDetails
from django.contrib.admin.widgets import AdminDateWidget


class fileDetailsAdminForm(forms.ModelForm):
    title           = forms.CharField(max_length=150)
    filetype        = forms.CharField(max_length=10, required=True,widget=forms.Select(choices=(('video', "Video"), ('img', 'Image'))))
    play_from       = forms.DateField(widget= AdminDateWidget)
    play_Till       = forms.DateField(widget= AdminDateWidget)
    play_duration   = forms.IntegerField()
    play_on_tv_id   = forms.ChoiceField(choices = [])
    file_path       = forms.FileField(required=True)

    def __init__(self, *args, **kwargs):
        super(fileDetailsAdminForm, self).__init__(*args, **kwargs)
        self.fields['play_on_tv_id'].choices = [(tv.tv_name, tv.tv_name) for tv in tvDetails.objects.all()]

    class Meta:
        model = fileDetails
        fields = '__all__'