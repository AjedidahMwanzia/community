from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Neighborhood(models.Model):
    view =  CloudinaryField("image")
    name = models.CharField(max_length=50,blank=True)
    location = models.CharField(max_length = 50,null = True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    occupants = models.ForeignKey(User, null = True,related_name='business')
    
    def save_hood(self):
        self.save()

    @classmethod
    def get_all_hoods(cls):
        hood = NeighborHood.objects.all()
        return hood
