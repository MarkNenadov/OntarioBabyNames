from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from web.models import Baby_Name_Year

def index( request ):
    return HttpResponse( "<h3>Ontario BabyNames</h3> This is a site developed by Mark Nenadov using Django and MySQL. It makes use of CSV data made available by the Ontario Government through the terms of the  <a href='http://www.ontario.ca/government/open-government-licence-ontario'>Open Government License</a>. The data has been imported into a MySQL database. You can find the source code for this website on Mark Nenadov's GitHub profile. The source code for this site doesn't include the data, which can be downloaded from Ontario open data." )

def nameDetails( request, nameId ):
    babyNameYear = get_object_or_404( Baby_Name_Year, id=nameId )
    return render( request, 'web/detail.html', {'babyNameYear': babyNameYear} )
