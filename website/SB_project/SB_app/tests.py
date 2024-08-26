from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Site


class SiteModelTests(TestCase):
    def test_site_can_be_saved(self):
        """Fails if a viable site cannot be saved."""

        site = Site(name="test_example", area=15)

        before = len(Site.objects.all())
        site.save()
        after = len(Site.objects.all())

        self.assertEqual(before+1, after)
    
    
    def test_area_is_not_negative(self):
        """Fails if a site with negative area can be saved."""

        site = Site(name="test_example", area=-5)
        with self.assertRaises(expected_exception=ValidationError):
            site.save()