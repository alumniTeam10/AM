from django.shortcuts import render
from django.http import HttpResponse
from Database.models import User,Student,Faculty,Alumni
from django.template import loader
from django.db.models import  Q

def get_row_set(type_of_user):
    if type_of_user=='student':
        row_set=Student.objects.all()
    elif type_of_user=='alumni':
        row_set = Alumni.objects.all()
    elif type_of_user=='faculty':
        row_set = Faculty.objects.all()

    return row_set

def get_ids_from_user(type_of_user,search_term):

    search_fields = ['username', 'email', 'first_name', 'last_name']

    fields = [f for f in search_fields]
    queries = [Q(**{str(f + '__icontains'): search_term}) for f in fields]

    qs = Q()
    for query in queries:
        qs = qs | query

    qs = qs & (Q(**{'user_type_flag__contains': type_of_user}))

    user = User.objects.filter(qs).values('pk')

    ids=[]

    for i in user:
        ids.append(i['pk'])

    return ids

def get_search_fields(type_of_user):

    if type_of_user=='student':
        search_fields = ['department_name', 'branch_name', 'course_name', 'admission_date']
    elif type_of_user=='alumni':
        search_fields = ['department_name', 'branch_name', 'course_name', 'admission_date','passout_date','current_organization_name','designation','role']
    elif type_of_user=='faculty':
        search_fields = ['department_name', 'designation']

    return search_fields

def get_filtered_ids(type_of_user, search_term, ids):

    search_fields=get_search_fields(type_of_user)

    fields = search_fields
    queries = [Q(**{str(f + '__icontains'): search_term}) for f in fields]

    qs = Q()
    for query in queries:
        qs = qs | query

    for id in ids:
        qs = qs | (Q(**{'user_id': id}))


    if type_of_user=='student':
        user = Student.objects.filter(qs)
    elif type_of_user=='alumni':
        user = Alumni.objects.filter(qs)
    elif type_of_user=='faculty':
        user = Faculty.objects.filter(qs)


    for i in user:
        ids.append(i.user_id)

    return ids


def get_filtered_row_set(type_of_user,search_term):

    user=get_ids_from_user(type_of_user,search_term)

    print '!!!!!!!!!!!!',user

    user=get_filtered_ids(type_of_user, search_term, user)

    queries = [Q(**{'user_id': id}) for id in user]
    qs = Q()
    for query in queries:
        qs = qs | query

    print qs, len(user),user

    if type_of_user=='student':
        row_set=Student.objects.filter(qs)
    elif type_of_user=='alumni':
        row_set = Alumni.objects.filter(qs)
    elif type_of_user=='faculty':
        row_set = Faculty.objects.filter(qs)

    for row in row_set:
        print '--------->',row.user_id

    return row_set


def connect(request,type_of_user):

    row_set=get_row_set(type_of_user)
    context={"all_data":row_set, "type_of_user":type_of_user}
    return render(request, 'AlumniManagement/connect.html',context)



def search(request,type_of_user):
    query=request.GET['search_box']

    if not query:
        row_set = get_row_set(type_of_user)
    else:
        row_set=get_filtered_row_set(type_of_user,query)

    context = {"all_data": row_set, "type_of_user": type_of_user}
    return render(request, 'AlumniManagement/connect.html', context)


def view(request,type_of_user):
    user= get_user_details(request.POST['view'],type_of_user)

    for row in user:
        print row.user_id.first_name

    context={'user_data':user,"type_of_user": type_of_user}
    return render(request, 'AlumniManagement/view.html', context)

def get_user_details(user_id,type_of_user):

    if type_of_user=='student':
        row_set=Student.objects.filter(user_id__username=user_id)
    elif type_of_user=='alumni':
        row_set = Alumni.objects.filter(user_id__username=user_id)
    elif type_of_user=='faculty':
        row_set = Faculty.objects.filter(user_id__username=user_id)


    return row_set