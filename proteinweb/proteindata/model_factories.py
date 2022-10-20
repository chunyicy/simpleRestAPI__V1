import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from .models import*


class OrganismFactory(factory.django.DjangoModelFactory):
    organism_taxa_ID ='568076'
    organism_clade_identifier = 'E'
    organism_scientific_genus_name = 'Metarhizium'
    organism_scientific_species_name = 'robertsii'

    class Meta:
        model = Organism


class PfamFactory(factory.django.DjangoModelFactory):
    pfam_domain_ID = 'PF02800'
    pfam_domain_description = 'Glyceraldehyde3-phosphatedehydrogenase: C-terminaldomain'

    class Meta:
        model = Pfam
   

class DomainFactory(factory.django.DjangoModelFactory):
    domain_ID = 'PF02800'
    domain_description = 'Glyceraldehyde 3-phosphate dehydrogenase catalytic domain'
    pfam_domain_ID = factory.SubFactory(PfamFactory)
    
    class Meta:
        model = Domain


class ProteinFactory(factory.django.DjangoModelFactory):
    protein_ID = 'A0A014PQC0'
    length_of_protein = 338
    domain_start_coordinate = 157
    domain_end_coordinate = 314
    domain_ID = factory.SubFactory(DomainFactory)
    organism_taxa_ID = factory.SubFactory(OrganismFactory)

    class Meta:
        model = Protein
