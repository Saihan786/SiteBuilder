from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Site
from .forms import SiteForm

# Create your views here.
def index(request):
    return HttpResponse("lol")


def homepage(request):
    if request.method == "POST":
        form = SiteForm(request.POST)
        context = {'form': form}
        
        if form.is_valid():
            print(form)
            return render(request, "SB_app/example.html", context)
        else:
            return HttpResponse("error with invalid form")

    elif request.method == "GET":
        form = SiteForm()
        context = {'form': form}

        return render(request, "SB_app/example.html", context)

    return render(request, template_name="SB_app/example.html", context=None)