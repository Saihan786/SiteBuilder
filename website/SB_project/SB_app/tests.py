from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Site
from .forms import SiteForm


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
    
    
    def test_name_is_unique(self):
        """Fails if two sites with the same names can be saved."""

        site = Site(name="test_example", area=15)
        site2 = Site(name="test_example", area=15)
        with self.assertRaises(expected_exception=ValidationError):
            site.save()
            site2.save()



class SiteFormTests(TestCase):
    def test_viable_form_is_valid(self):
        """Fails if a form that should be valid returns False for form.isValid()."""
        
        form_data = {'name': 'test_example', 'area': 15}
        form = SiteForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        
    def test_negative_area_is_not_valid(self):
        """Fails if a form with negative area returns True for form.isValid()."""

        form_data = {'name': 'test_example', 'area': -5}
        form = SiteForm(data=form_data)
        self.assertFalse(form.is_valid())



class HomepageViewTests(TestCase):
    def test_GET(self):
        """Fails if a GET request has a status code that isn't 200."""
        response = self.client.get( reverse('homepage') )
        self.assertEqual(response.status_code, 200)

        
    def test_POST(self):
        """Fails if a POST request has a status code that isn't 200."""
        response = self.client.post( reverse('homepage') )
        self.assertEqual(response.status_code, 200)
    
    
    def test_empty_form(self):
        """Fails if an empty form is NOT shown for a GET request."""

        response = self.client.get( reverse('homepage') )
        self.assertContains(response, "Name:")
        self.assertContains(response, "Area:")
        self.assertContains(response, "Add site")
    
    
    def test_valid_form(self):
        """Fails if the correct text isn't shown when a valid form is
        submitted."""

        form_data = {'name': 'test_example', 'area': 15}
        response = self.client.post( reverse('homepage'), data=form_data )

        self.assertContains(response, "Name:")
        self.assertContains(response, "Area:")
        self.assertContains(response, "Add site")
        self.assertContains(response, "You've submitted a form!")
    
    
    def test_invalid_form(self):
        """Fails if the correct text isn't shown when an invalid form is
        submitted."""

        form_data = {'name': 'test_example', 'area': -5}
        response = self.client.post( reverse('homepage'), data=form_data )

        self.assertContains(response, "Name:")
        self.assertContains(response, "Area:")
        self.assertContains(response, "Add site")
        self.assertContains(response, "You've submitted the form wrong!")
    
    
    def test_matching_name(self):
        """Fails if the correct text isn't shown when the name in a form
        matches the name of an already-existing site."""
        
        site = Site(name="test_example", area=15)
        site.save()

        form_data = {'name': 'test_example', 'area': 15}
        response = self.client.post( reverse('homepage'), data=form_data )

        self.assertContains(response, "Name:")
        self.assertContains(response, "Area:")
        self.assertContains(response, "Add site")
        self.assertContains(response, "A site with that name already exists.")