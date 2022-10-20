from rest_framework import serializers
from .models import *

# inheriting from ModelSerializer
class PfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pfam 
        fields = ['id','pfam_domain_ID', 'pfam_domain_description']


class DomainSerializer(serializers.ModelSerializer):
    pfam_domain_ID = PfamSerializer()
    class Meta: 
        model = Domain # specify the fields to be served to the user/ uploaded by user
        fields = ['id','domain_ID','domain_description','pfam_domain_ID']

        def create(self, validated_data):
            pfam_data = self.initial_data.get('pfam_domain_ID')
            domain = Domain(**{**validated_data, 
                        'pfam_domain_ID': Pfam.objects.get(pk = pfam_data['id'])})
            domain.save() # save new data
            return domain


class OrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organism # model from Organism class
        fields = ['id','organism_taxa_ID','organism_clade_identifier','organism_scientific_genus_name',
                  'organism_scientific_species_name']


class ProteinSerializer(serializers.ModelSerializer):
    domain_ID = DomainSerializer()
    organism_taxa_ID = OrganismSerializer()
    class Meta:
        model = Protein # model from the Protein class

        # specify the fields to be served to the user 
        fields = ['protein_ID', 'length_of_protein', 'domain_start_coordinate', 'domain_end_coordinate', 
                  'domain_ID', 'organism_taxa_ID']
    
    def create(self, validated_data):
        domain_data = self.initial_data.get('domain_ID') # get copy of the domain data
        organism_data = self.initial_data.get('organism_taxa_ID') # get a copy of the organism data
        protein = Protein(**{**validated_data, 
                         # ensure the domain data id is the correct object
                         # to ensure the data that get from the user is assign to the correct foreign key 
                        'domain_ID': Domain.objects.get(pk=domain_data['id']), 
                        'organism_taxa_ID': Organism.objects.get(pk = organism_data['id'])})
        protein.save()
        return protein





class OrganismProteinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['id','protein_ID']


class OrganismPfamSerializer(serializers.ModelSerializer):
    id= serializers.CharField(source='domain_ID.pfam_domain_ID.id')
    pfam_domain_ID= serializers.CharField(source='domain_ID.pfam_domain_ID.pfam_domain_ID')
    pfam_domain_description= serializers.CharField(source='domain_ID.pfam_domain_ID.pfam_domain_description')

    class Meta:
         model = Protein
         fields = ['id','pfam_domain_ID', 'pfam_domain_description']

