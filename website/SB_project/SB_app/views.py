from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Site, HouseTypes
from .forms import SiteForm, HouseTypeForm

homepage_template_url = "SB_app/homepage.html"
settings_template_url = "SB_app/settings.html"
htl_template_url = "SB_app/housetype_library.html"


# Create your views here.
def index(request):
    return render(request, "SB_app/index.html", context=None)


def homepage(request):
    site_objects = Site.objects.all()
    context = {'site_objects': site_objects}
    
    if request.method == "POST":
        form = SiteForm(request.POST)
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data.get('name')
            area = form.cleaned_data.get('area')

            try:
                Site(name=name, area=area).save()
                context['valid_form'] = True
            except Exception as e:
                unique_name_error = 'Site with this Name already exists.'
                if unique_name_error in e.messages:
                    context['name_violation'] = True
            
            return render(request, homepage_template_url, context)
        else:
            context['invalid_form'] = True
            return render(request, homepage_template_url, context)

    elif request.method == "GET":
        form = SiteForm()
        context['form'] = form

        return render(request, homepage_template_url, context)

    return render(request, template_name=homepage_template_url, context=None)


def settings(request):
    return render(request, template_name=settings_template_url, context=None)


def htl(request):
    ht_objects = HouseTypes.objects.all()
    context = {'ht_objects': ht_objects}
    
    if request.method == "POST":
        form = HouseTypeForm(request.POST)
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data.get('name')
            print(name)

            try:
                HouseTypes(name=name).save()
                context['valid_form'] = True
            except Exception as e:
                print(e)
                unique_name_error = 'HouseTypes with this Name already exists.'
                if unique_name_error in e.messages:
                    context['name_violation'] = True
            
            return render(request, htl_template_url, context)
        else:
            context['invalid_form'] = True
            return render(request, htl_template_url, context)

    elif request.method == "GET":
        form = HouseTypeForm()
        context['form'] = form

        return render(request, htl_template_url, context)

    return render(request, template_name=htl_template_url, context=None)