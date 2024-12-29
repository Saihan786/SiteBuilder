import django_tables2 as tables
from .models import Site

class SiteTable(tables.Table):
    """
    Table containing all Site objects that the user makes.

    TBD:
        - Add search bar
        - Add multiple pages on table    
    """

    class Meta():
        model = Site
        template_name = "tables/site_table.html"