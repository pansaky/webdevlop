# -*- coding = utf-8 -*-
from django.shortcuts import render
from . import models

# Create your views here.
def baby(request):
    #dbmodel = models.dbmodel.from_db()
    return render(request, 'root.html')

def wife(request):
    return render(request, 'root.html', {'TOB': 'Love my baby!'})