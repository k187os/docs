from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse

from clinic.forms import PatientForm
from clinic.models import Patient, Consultation
from clinic.templatetags.clinic_extras import search_p


@login_required
def index(request):
    patient_list = Patient.objects.order_by('-Nom')[:3]
    cc = Consultation.objects.count()
    pc = Patient.objects.count()
    context_dict = {'patientcount': Patient.objects.count()}
    return render(request, 'clinic/index.html', {'list_patient': patient_list, 'counscount': cc ,'patientcount': pc})


@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            upper = form.save(commit=False)
            upper.Nom = upper.Nom.upper()
            upper.Prenom = upper.Prenom.upper()
            dn = upper.Date_Naissance
            patient_list = Patient.objects.filter(Date_Naissance=dn)
            if patient_list:
                for wew in patient_list:
                    if wew.Nom == upper.Nom and wew.Prenom == upper.Prenom and wew.Date_Naissance == dn:
                        return HttpResponse('ALREADY EXIST')
                    else:
                        upper.save()
            else:
                upper.save()
            return patients_list(request)
        else:
            print(form.errors)
            # return render(request, 'clinic/add_patient.html', {, 'fault': form.errors})
    else:
        form = PatientForm()
    return render(request, 'clinic/add_patient.html', {'form': form})


@login_required
def patients_list(request):
    if request.method == 'GET':
        if 'searchpatient' in request.GET:
            pts = request.GET['searchpatient']
            patient_list = Patient.objects.filter(Nom__istartswith=pts)
        else:
            patient_list = Patient.objects.order_by('-id')
    else:
        patient_list = Patient.objects.order_by('-id')
    paginator = Paginator(patient_list, 10)
    page = request.GET.get('page')
    try:
        plist = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        plist = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        plist = paginator.page(paginator.num_pages)

    context_dict = {'list_patient': plist}
    return render(request, 'clinic/patients_list.html', context_dict)


@login_required
def consultation(request):
    cons_list = Consultation.objects.order_by('-id')
    # patients_list = Patient.objects.all()
    context_dict = {'list_consultation': cons_list}
    return render(request, 'clinic/consultation.html', context_dict)


def add_consultation(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            upper = form.save(commit=False)
            upper.Nom = upper.Nom.upper()
            upper.Prenom = upper.Prenom.upper()
            dn = upper.Date_Naissance
            patient_list = Patient.objects.filter(Date_Naissance=dn)
            if patient_list:
                for wew in patient_list:
                    if wew.Nom == upper.Nom and wew.Prenom == upper.Prenom and wew.Date_Naissance == dn:
                        return HttpResponse('ALREADY EXIST')
                    else:
                        upper.save()
            return patients_list(request)
        else:
            print(form.errors)
    else:
        form = PatientForm()
    return render(request, 'clinic/add_patient.html', {'form': form})


def patients(request, pt_id):
    pat_dict = {}
    try:
        pat = Patient.objects.get(id=pt_id)
        pat_dict['patient'] = pat
    except Patient.DoesNotExist:
        pass
    return render(request, 'clinic/patient.html', pat_dict)


def search_patients(request):
    pat_list = []
    starts_with = ''
    if request.method == 'GET':
        if 'p' in request.GET:
            starts_with = request.GET['p']
            pat_list = search_p(8, starts_with)

    return render(request, 'clinic/pats.html', {'pat_list': pat_list})


def testing(request):
    return render(request, 'clinic/test.html')
