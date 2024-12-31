import django_tables2 as tables
from .models import Site, HouseTypes

class SiteTable(tables.Table):
    """
    Table containing all Site objects that the user makes.

    TBD:
        - Add search bar
    """

    class Meta():
        model = Site
        template_name = "django_tables2/bootstrap5.html"
        fields = ("name", "area",)


class HTLTable(tables.Table):
    """
    Table containing all HouseType objects that the user makes.
    
    Represents the housetype library.

    """

    class Meta():
        model = HouseTypes
        template_name = "django_tables2/bootstrap5.html"
        fields = ("name", "configuration", "beds", "storeys", "sales_sq_ft", "build_sq_ft", "build_cost", "build_cost_divide_sq_ft", "build_Weeks", "depth", "width", "NDSS", "NDSS_Description", "Accessibility", "parking_spaces",)
