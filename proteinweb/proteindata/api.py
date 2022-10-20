from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# takes a list of the different HTTP methods
@api_view(['GET','POST']) 

def protein_detail(request, type): # requests object and the protein type from the user
    if request.method == 'POST': # passing data coming from the user into the ProteinSerializer
        serializer = ProteinSerializer(data=request.data)
        if serializer.is_valid(): # to check if the data is correct
            serializer.save() # save new data
            return Response(serializer.data, status=status.HTTP_201_CREATED) # return HTTP 201 created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        # filter to get protein from database based on the protein type
        protein = Protein.objects.filter(protein_ID__exact=type)

    except Protein.DoesNotExist: 
        return HttpResponse(status=404) # return 404 response for missing data

    if request.method == 'GET': # successfully get the protein data
        serializer = ProteinSerializer(protein, many=True)  # called the ProteinSerializer 
        return Response(serializer.data)  # return the serialize data
        
        
        
# GET request
@api_view(['GET']) 
def pfam_detail(request, type):
    try: # filter by pfam ID
        pfam = Pfam.objects.filter(pfam_domain_ID__exact=type)
        
    except Pfam.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET': # check what did the user request
        serializer = PfamSerializer(pfam, many=True) # serialize the data, call the pfamserializer 
        # and we pass in the row of data that we hopefully successfully got earlier
        # we got the serialize object, this is the kind of json string that will be
        # sent to the user
        return Response(serializer.data) # return serialize data to user


@api_view(['GET'])

def organismProtein_detail(request, type):
    try:
        # get the protein organism taxa id that is match with the string type that the user requested
        proteins = Protein.objects.filter(organism_taxa_ID__organism_taxa_ID__exact=type)
        
    except Protein.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = OrganismProteinSerializer(proteins, many=True)
        return Response(serializer.data)




@api_view(['GET'])

def organismPfam_detail(request, type):
    try:
        proteins = Protein.objects.filter(organism_taxa_ID__organism_taxa_ID__exact=type)
        
    except Protein.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = OrganismPfamSerializer(proteins, many=True) # many lists
        return Response(serializer.data)

