from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import*
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView

from .form import ProteinForm


def index(request):
    return render(request, 'proteindata/index.html')


def proteinList(request):
    # finding single protein from the table
    # using the object based on the protein id
    # using distinct() to get unique value of each id
    proteins = Protein.objects.values('protein_ID').distinct()
    return render(request, 'proteindata/protein_list.html', {'proteins': proteins })



def proteinDetail(request, type):
    # finding single protein from the table
    # filter protein object by it's protein id to get all details of each protein
    proteins = Protein.objects.filter(protein_ID__exact=type)
    return render(request, 'proteindata/protein_detail.html', {'proteins': proteins,'type':type })


class pfamList(ListView):
    # displayed a list of the pfam model
    model = Pfam
    context_object_name = 'pfams'
    template_name='proteindata/pfam_list.html'

    
def pfamDetail(request, type):
    # getting each pfam details from the table
    # using the object based on the pfam domain id
    pfams = Pfam.objects.filter(pfam_domain_ID__exact=type)
    return render(request, 'proteindata/pfam_detail.html', {'pfams': pfams,'type':type })


def organismProteinList(request):
    organisms = Organism.objects.values('organism_taxa_ID').distinct()
    return render(request, 'proteindata/organism_proteinList.html', {'organisms': organisms })



def organismPfamList(request):
    organisms = Organism.objects.values('organism_taxa_ID').distinct()
    return render(request, 'proteindata/organism_pfamList.html', {'organisms': organisms })



def organismProteinDetail(request, type):
    proteins = Protein.objects.filter(organism_taxa_ID__organism_taxa_ID__exact=type)
    return render(request, 'proteindata/organismProtein_detail.html', {'proteins': proteins, 'type':type })




def organismPfamDetail(request, type):
    proteins = Protein.objects.filter(organism_taxa_ID__organism_taxa_ID__exact=type)
    return render(request, 'proteindata/organismPfam_detail.html', {'proteins': proteins, 'type':type })



class ProteinCreate(CreateView):
    model = Protein
    template_name = 'proteindata/create_protein.html'
    form_class = ProteinForm
    success_url = "create_protein"

