from Database.models import User,DocumentType,UserDocumentMap
from django.template import loader
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
def UserDocuments(request):
    #user=User.objects.all()
    documentTypeValues = DocumentType.objects.all()
    #return HttpResponse("<h1>hiii</h1>")
    html='<select>'
    documentTypeValues=DocumentType.objects.all()
    #print(documentTypeValues.len())
    for documentTypeObj in documentTypeValues :
        html+=' <option value='+documentTypeObj.document_type+'>'+documentTypeObj.document_type+'</option> '
    return HttpResponse("Document Type:"+html+'</select>')
    #return HttpResponse(documentTypeObj.document_type)
    #return HttpResponse("<div class='col-md-2 place-grid'><select class='sel'><option value='Trascripts'>Document Type</option></select></div><h2>Document Value="+str(document_id)+"</h2>")