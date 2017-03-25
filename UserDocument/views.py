from Database.models import User,DocumentType,UserDocumentMap
from django.template import loader
from django.db.models import Q
from django.shortcuts import render
def UserDocuments(request,typeOfDocument):
    #row_set=get_row_set(typeOfDocument)
    #context={"all_data":row_set, "type_of_user":type_of_user}
    context="<h1>testing</h1>"
    return render(request, 'web/contact.html',context)