from django.shortcuts import render
from django.apps import apps
import json
from django.shortcuts import render, redirect
from django.apps import apps
import json

from .forms import ProgForm

jsnfile = apps.get_app_config('recrutement').path + '/json-data/programme.json'

def ProgrammeList(request):
    with open(jsnfile) as pr:
        prog = json.load(pr)
    return render(request, 'programme.html', {'pr':prog})


def AjouterProgramme(request):
    if request.method == 'GET':
        return render(request, 'ajouter_prog.html', {'pr':{}})
    if request.method == 'POST':
        form = ProgForm(request.POST)
        if form.is_valid():
            fa= form.cleaned_data.get("id")
            name= form.cleaned_data.get("name")
            price= form.cleaned_data.get("price")
            appartements= form.cleaned_data.get("appartements")
            nbr = form.cleaned_data.get("nbr")
            cr = form.cleaned_data.get("cr")

        with open(jsnfile) as cr:
            prr = json.load(cr)
        prr.append({"id": str(fa), "name": name, "Appartement": appartements, "price": price , "Nombre de Pieces" : nbr })
        with open(jsnfile, 'w') as cw:
            json.dump(prr, cw)
        return redirect(ProgrammeList)