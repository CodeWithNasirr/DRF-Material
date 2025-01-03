import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Home.settings'
django.setup()
# Create your tests here.
from django.apps import apps



def get_all_models():
    for model in apps.get_models:
        print(model.__name__)

get_all_models()