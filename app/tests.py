from django.test import TestCase

from app.models import  AcaoAtpModel 
from django.contrib.auth.decorators import login_required
from .decorators import check_user_is_authenticated, user_required
import pandas as pd
# Create your tests here.



#### tesntando import pandas links uteis
'https://www.geeksforgeeks.org/rendering-data-frame-to-html-template-in-table-view-using-django-framework/'
'https://pypi.org/project/django-pandas/'
'https://studygyaan.com/django/pandas-in-django'
'https://hackershrine.com/machine-learning/render-pandas-dataframe-on-your-django-webapp/'
