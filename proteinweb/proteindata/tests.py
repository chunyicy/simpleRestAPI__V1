import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .model_factories import *
from .serializers import*


class ProteinTest(APITestCase):

    def test_proteinDetailReturnSuccess(self):
        protein = ProteinFactory.create(pk=10003, protein_ID = "A0A014PQC0")
        url = reverse('protein_api', kwargs={'type': 'A0A014PQC0'})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)

    # def test_proteinDetailReturnFailOnBadPk(self):
    #     protein = ProteinFactory.create(pk=10003, protein_ID='A0A014PQC0')
    #     url = '/api/protein/H'
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code,404)


class ProteinSerialiserTest(APITestCase):
    protein1=None
    proteinSerializer = None

    def setUp(self):
        self.protein1 = ProteinFactory.create(pk=10003, protein_ID='A0A014PQC0')
        self.proteinSerializer = ProteinSerializer(instance = self.protein1)
    def tearDown(self):
        Pfam.objects.all().delete()
        Domain.objects.all().delete()
        Organism.objects.all().delete()
        Protein.objects.all().delete()

        PfamFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)
        OrganismFactory.reset_sequence(0)
        ProteinFactory.reset_sequence(0)

    def test_proteinSerializer(self):
        data=self.proteinSerializer.data
        self.assertEqual(set(data.keys()), set(['protein_ID', 'length_of_protein', 
                 'domain_start_coordinate', 'domain_end_coordinate', 
                  'domain_ID', 'organism_taxa_ID']))
        self.assertEqual(data['protein_ID'], 'A0A014PQC0')

