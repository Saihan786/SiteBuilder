from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Site, HouseTypes
from .forms import SiteForm, HouseTypeForm
from .tables import SiteTable, HTLTable

homepage_template_url = "SB_app/homepage.html"
settings_template_url = "SB_app/settings.html"
htl_template_url = "SB_app/housetype_library.html"


def index(request):
    return render(request, "SB_app/index.html", context=None)


def homepage(request):
    site_objects = Site.objects.all()
    site_table = SiteTable(data=site_objects)

    context = {'site_objects': site_objects, 'site_table': site_table}
    
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
            
            site_table.paginate(page=request.POST.get("page", 1), per_page=7)
            return render(request, homepage_template_url, context)
        else:  
            context['invalid_form'] = True
            return render(request, homepage_template_url, context)

    elif request.method == "GET":
        site_table.paginate(page=request.GET.get("page", 1), per_page=7)
        form = SiteForm()
        context['form'] = form

        return render(request, homepage_template_url, context)

    return render(request, template_name=homepage_template_url, context=context)


def settings(request):
    context = {}
    if request.method == "POST":
        pass

    elif request.method == "GET":
        return render(request, settings_template_url, context)

    return render(request, template_name=settings_template_url, context=context)


def htl(request):
    housetype_objects = HouseTypes.objects.all()
    housetype_table = HTLTable(data=housetype_objects)

    context = {'housetype_objects': housetype_objects, 'housetype_table': housetype_table}

    if request.method == "POST":
        form = HouseTypeForm(request.POST)
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data.get('name')
            configuration = form.cleaned_data.get('configuration')
            beds = form.cleaned_data.get('beds')
            storeys = form.cleaned_data.get('storeys')
            sales_sq_ft = form.cleaned_data.get('sales_sq_ft')
            build_sq_ft = form.cleaned_data.get('build_sq_ft')
            build_cost = form.cleaned_data.get('build_cost')
            build_cost_divide_sq_ft = form.cleaned_data.get('build_cost_divide_sq_ft')
            build_weeks = form.cleaned_data.get('build_weeks')
            depth = form.cleaned_data.get('depth')
            width = form.cleaned_data.get('width')
            NDSS = form.cleaned_data.get('NDSS')
            NDSS_Description = form.cleaned_data.get('NDSS_Description')
            Accessibility = form.cleaned_data.get('Accessibility')
            parking_spaces = form.cleaned_data.get('parking_spaces')
            plotting_sq_ft = form.cleaned_data.get('plotting_sq_ft')

            try:
                HouseTypes(
                    name=name,
                    configuration=configuration,
                    beds=beds,
                    storeys=storeys,
                    sales_sq_ft=sales_sq_ft,
                    build_sq_ft=build_sq_ft,
                    build_cost=build_cost,
                    build_cost_divide_sq_ft=build_cost_divide_sq_ft,
                    build_weeks=build_weeks,
                    depth=depth,
                    width=width,
                    NDSS=NDSS,
                    NDSS_Description=NDSS_Description,
                    Accessibility=Accessibility,
                    parking_spaces=parking_spaces,
                    plotting_sq_ft=plotting_sq_ft,
                ).save()
                context['valid_form'] = True
            except Exception as e:
                unique_name_error = 'House type with this Name already exists.'
                if unique_name_error in e.messages:
                    context['name_violation'] = True
            
            housetype_table.paginate(page=request.POST.get("page", 1), per_page=7)
            return render(request, htl_template_url, context)
        else:  
            context['invalid_form'] = True
            return render(request, htl_template_url, context)


    elif request.method == "GET":
        housetype_table.paginate(page=request.GET.get("page", 1), per_page=7)
        form = HouseTypeForm()
        context['form'] = form

        return render(request, htl_template_url, context)

    return render(request, template_name=htl_template_url, context=context)