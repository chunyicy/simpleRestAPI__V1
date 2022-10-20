import os
import sys
import django
import csv
from collections import defaultdict
sys.path.append("/Users/user/Desktop/advanced web dev/project/midtermCW/proteinweb")

os.environ.setdefault('DJANGO_SETTINGS_MODULE','proteinweb.settings')

django.setup()

from proteindata.models import *
data_file = '/Users/user/Desktop/advanced web dev/project/midtermCW/assignment_data_set.csv'
pfam_file = '/Users/user/Desktop/advanced web dev/project/midtermCW/pfam_descriptions.csv'
dataSeq_file = '/Users/user/Desktop/advanced web dev/project/midtermCW/assignment_data_sequences.csv'

# stroring a list of data
organism = []
pfam = []
domain = []
protein = []

# open data file
with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader :

        # Organism Taxa ID - row 1
        # Organism Clade Idenitifer - row 2
        # Organism Scientific name ("Genus Species") - row 3
        organism_scientific_name = row[3]
        data = organism_scientific_name.split() # splitting the name 
        organism.append((row[1], row[2], data[0], data[1])) 
        
        # Protein ID - row 0
        # Length of Protein - row 8
        # Domain Start Coordinate - row 6
        # Domain End Coordinate - row 7
        # row 5 - domain id
        # Organism Taxa ID - row 1
        protein.append((row[0],row[8], row[6], row[7], row[5],row[1]))

        # Domain ID - row 5
        # Domain description - row 4
        domain.append((row[5], row[4]))
       

with open(pfam_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        # pfam id - row 0
        # pfam description - row 1
        pfam.append((row[0], row[1]))


Organism.objects.all().delete()
Pfam.objects.all().delete()
Domain.objects.all().delete()
Protein.objects.all().delete()


organism_rows = {} # storing foreign key
pfam_rows={}
domain_rows = {}
protein_rows = {}


# insert data into Organism table
for data in organism:
    row = Organism.objects.create(organism_taxa_ID=data[0],
                                  organism_clade_identifier=data[1],
                                  organism_scientific_genus_name=data[2],
                                  organism_scientific_species_name=data[3])
    row.save()
    organism_rows[data[0]] = row


# insert data into Pfam table
for data in pfam:
    row = Pfam.objects.create(pfam_domain_ID = data[0],
                              pfam_domain_description = data[1])

    row.save()
    pfam_rows[data[0]] = row


# insert data into Domain table
for data in domain:
    row = Domain.objects.create( domain_ID=data[0],
                                 domain_description = data[1],
                                 pfam_domain_ID=pfam_rows[data[0]])
                                
    row.save()
    domain_rows[data[0]] = row


# insert data into Protein table
for data in protein:
    row = Protein.objects.create(protein_ID=data[0],
                                 length_of_protein=data[1],
                                 domain_start_coordinate=data[2],
                                 domain_end_coordinate=data[3],
                                 domain_ID = domain_rows[data[4]],
                                 organism_taxa_ID=organism_rows[data[5]])
    row.save()
    protein_rows[data[0]] = row




