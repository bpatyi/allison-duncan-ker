from django import forms

from menu.models import MenuItem


class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem

    def clean(self):
        cleaned_data = super(MenuItemForm, self).clean()

        url = cleaned_data.get('url', 'None')
        flatpage = cleaned_data.get('flatpage', 'None')

        if url and flatpage:
            raise forms.ValidationError(u"Please, just fill in one field only. Flatpage or Url.")

        if not(url or flatpage):
            raise forms.ValidationError(u"Please, fill in flatpage or url field.")

        return cleaned_data