from django import forms
from django.forms import ModelForm, TextInput
from ietf.codestand.matches.models import ProjectContainer, CodingProject, Implementation, ProjectContact


class SearchForm(forms.Form):
    search = forms.CharField(label="Search", max_length=255, required=False)


class LinkImplementationForm(ModelForm):
    class Meta:
        model = Implementation
        fields = ["link"]
        
        widgets = {
            'link': TextInput(attrs={'placeholder': 'Enter url here'})
        }


class ContactForm(ModelForm):
    class Meta:
        model = ProjectContact
        fields = ["contact", "type"]
        
        widgets = { 
            'contact': TextInput(attrs={'placeholder': 'Enter contact here'})
        }


class ProjectContainerForm(ModelForm):
    class Meta:
        model = ProjectContainer
        fields = ["title", "protocol", "description"]
        
        widgets = { 
            'title': TextInput(attrs={'placeholder': 'Enter project title here'}),
            'protocol': TextInput(attrs={'placeholder': 'Enter protocol here'}),
            'description': TextInput(attrs={'placeholder': 'Enter description here'})
        }


class CodingProjectForm(ModelForm):
    class Meta:
        model = CodingProject
        fields = ["title", "additional_information"]
        
        widgets = { 
            'title': TextInput(attrs={'placeholder':'Enter coding title here'}),
            'additional_information': TextInput(attrs={'placeholder': 'Enter coding information here'})
        }
