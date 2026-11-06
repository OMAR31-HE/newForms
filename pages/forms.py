
from django import forms
from .models import Student
import re


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    def clean_name(self):
        name = self.cleaned_data['name']

        if not re.fullmatch(r"[A-Za-z ]+", name):
            raise forms.ValidationError(
                "Name must contain letters and spaces only."
            )

        return name

    def clean_university_id(self):
        university_id = self.cleaned_data['university_id']

        if len(str(university_id)) != 9:
            raise forms.ValidationError(
                "University ID must contain exactly 9 digits."
            )
#
        if str(university_id)[0] not in ['1', '2']:
            raise forms.ValidationError(
                "University ID must start with 1 or 2."
            )

        return university_id

    def clean_id_number(self):
        id_number = self.cleaned_data['id_number']

        if len(str(id_number)) != 9:
            raise forms.ValidationError(
                "ID Number must contain exactly 9 digits."
            )

        if str(id_number)[0] not in ['9', '8', '4']:
            raise forms.ValidationError(
                "ID Number must start with 9, 8, or 4."
            )

        return id_number

    def clean_mobile_number(self):
        mobile = self.cleaned_data['mobile_number']

        if not re.fullmatch(r"05[69]\d{7}", mobile):
            raise forms.ValidationError(
                "Mobile must be 10 digits and start with 059 or 056."
            )

        return mobile

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            extension = image.name.lower().rsplit('.', 1)[-1]

            if extension not in ['jpg', 'png']:
                raise forms.ValidationError(
                    "Only JPG and PNG images are allowed."
                )

        return image
