from django.test import TestCase
from django.test import Client
from django.utils import timezone
from bugs.models import Bugs
from django.urls import reverse

class Testmodels(TestCase):
    
    def setUp(self):
        self.bug1 =  Bugs.objects.create(
            description = "bug in the code",
            bug_type = "error in css display",
            report_date = timezone.now(),
            status = 'on going'
        )
    
    def test_bug_is_assign_description(self):
        self.assertEqual(self.bug1.description,'bug in the code')
        
    
    def test_bug_is_assign_bugtype(self):
        self.assertEqual(self.bug1.bug_type,'error in css display')
        
        
    def test_bug_is_assign_status(self):
        self.assertEqual(self.bug1.status,'on going')
        
    
    def test_description_max_length(self):
        self.bug1 = Bugs.objects.get(id=1)
        max_length = self.bug1._meta.get_field('description').max_length
        self.assertEqual(max_length, 200)
        
    
  
    