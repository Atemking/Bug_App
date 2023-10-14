from django.test import TestCase
from django.test import Client
from django.utils import timezone
from bugs.models import Bugs
from django.urls import reverse


class testViews(TestCase):
    
    def setUp(self):
        self.bug1 =  Bugs.objects.create(
            description = "bug in the code",
            bug_type = "error in css display",
            report_date = timezone.now(),
            status = 'on going'
        )
    
    
    
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('bugs/register')
        self.assertEqual(response.status_code, 404)
    
    def test_view_url_exists_at_desired_location_tab(self):
        response = self.client.get('TableView')
        self.assertEqual(response.status_code, 404)
    
    def test_view_url_exists_at_desired_location_disp(self):
        response = self.client.get('display')
        self.assertEqual(response.status_code, 404)
        
    def test_view_url_exists_at_desired_location_home(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 404)
    
    
        
    