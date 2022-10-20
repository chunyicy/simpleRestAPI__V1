from django.db import models

# organism table
class Organism(models.Model):
    # charfield contain strings, set maximum character length
    organism_taxa_ID = models.CharField(max_length=256, null=False,blank=True, db_index=True)
    organism_clade_identifier = models.CharField(max_length=256, null=False, blank=True)
    organism_scientific_genus_name = models.CharField(max_length=256, null=False, blank=True)
    organism_scientific_species_name = models.CharField(max_length=256, null=False, blank=True)

    def __str__(self):
        return self.organism_taxa_ID


# Pfam table
class Pfam(models.Model):
    # blank = False, null = False -> unique ID column should not set to null or black
    pfam_domain_ID = models.CharField(max_length=256, null=False,blank=False)
    pfam_domain_description = models.CharField(max_length=256, null=False,blank=False)

    def __str__(self):
            return self.pfam_domain_description 


# Domain table
class Domain(models.Model):
    domain_ID = models.CharField(max_length=256, null=False,blank=False)
    domain_description = models.CharField(max_length=256, null=False,blank=False)
    pfam_domain_ID = models.ForeignKey(Pfam, on_delete=models.DO_NOTHING) # foreign key, reference Pfam table

    def __str__(self):
        return self.domain_ID


# Protein table 
class Protein(models.Model):
    protein_ID =models.CharField(max_length=256, null=False,blank=True)
    length_of_protein = models.IntegerField(null=False, blank=True)
    domain_start_coordinate = models.IntegerField(null=False, blank=True) # store integer
    domain_end_coordinate = models.IntegerField(null=False, blank=True)
    domain_ID =models.ForeignKey(Domain, on_delete=models.DO_NOTHING) # foreign key, reference Domain table
    organism_taxa_ID = models.ForeignKey(Organism, on_delete=models.DO_NOTHING) # foreign key, reference Organism table

    def __str__(self):
        return self.protein_ID 
