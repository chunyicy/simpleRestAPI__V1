from django import forms
from django.forms import ModelForm
from .models import *


class ProteinForm(ModelForm):
    class Meta:
        model = Protein
        fields = ['protein_ID','length_of_protein','domain_start_coordinate','domain_end_coordinate','domain_ID','organism_taxa_ID']

        def clean(self):
            cleaned_data=super(ProteinForm, self).clean()
            