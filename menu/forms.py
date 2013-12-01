from django import forms

from menu.models import MenuItem


class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem

    def clean(self):
        cleaned_data = super(MenuItemForm, self).clean()

        url = cleaned_data.get('url', 'None')
        flatpage = cleaned_data.get('flatpage', 'None')
        section = cleaned_data.get('section', 'None')

        if url and flatpage or url and section or flatpage and section:
            raise forms.ValidationError(u"Please, just fill in one field only. Flatpage or Url or Section.")

        if not(url or flatpage or section):
            raise forms.ValidationError(u"Please, fill in flatpage, section, or url field.")

        return cleaned_data