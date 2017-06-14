from django import template
from clinic.models import Patient

register = template.Library()

@register.inclusion_tag('clinic/pats.html')
def search_p(max_results=0, starts_with=''):
    pat_list=[]
    if starts_with:
        pat_list = Patient.objects.filter(Nom__istartswith=starts_with)

    if pat_list and max_results > 0:
        if pat_list.count() > max_results:
            pat_list = pat_list[:max_results]

    return pat_list
