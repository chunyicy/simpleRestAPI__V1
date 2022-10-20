
from django.contrib import admin
from .models import*

# use ModelAdmin objects to add display columns
class OrganismAdmin(admin.ModelAdmin):
    list_display = ('organism_taxa_ID', 'organism_clade_identifier','organism_scientific_genus_name', 'organism_scientific_genus_name')

class PfamAdmin(admin.ModelAdmin):
    list_display = ('pfam_domain_ID','pfam_domain_description')

class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain_ID','domain_description', 'pfam_domain_ID')

class ProteinAdmin(admin.ModelAdmin):
    list_display = ('protein_ID','length_of_protein','domain_start_coordinate','domain_end_coordinate','domain_ID','organism_taxa_ID')

# register the model class
admin.site.register(Organism, OrganismAdmin)
admin.site.register(Pfam, PfamAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Protein, ProteinAdmin)

