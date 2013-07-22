from django.db import models

# Create your models here.

class Baby_Name_Year( models.Model ):
    year = models.IntegerField( default=0 )
    name = models.CharField( max_length=50 )
    gender = models.CharField( max_length=1 )
    occurances = models.IntegerField( default=0 )

    def __unicode__( self ):
        return self.name + " (" + str(self.year) + ") "
