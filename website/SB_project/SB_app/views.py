from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Site
from .forms import SiteForm

# Create your views here.
def index(request):
    return HttpResponse("lol")


def homepage(request):
    homepage_template_url = "SB_app/example.html"
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