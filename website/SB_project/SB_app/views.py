from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Site
from .forms import SiteForm

# Create your views here.
def index(request):
    return HttpResponse("lol")


def homepage(request):
    homepage_template_url = "SB_app/example.html"
    
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            context = {
                'form': form,
                'valid_form': True,
            }
            return render(request, homepage_template_url, context)
        else:
            context = {
                'form': form,
                'invalid_form': True,
            }
            return render(request, homepage_template_url, context)

    elif request.method == "GET":
        form = SiteForm()
        context = {'form': form}

        return render(request, homepage_template_url, context)

    return render(request, template_name=homepage_template_url, context=None)