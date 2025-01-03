import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'DRF.settings'
django.setup()
# Create your tests here.
from django.apps import apps



def get_model_config(model_name):
    models=None
    for app_config in apps.get_app_configs():
        try:
            models=apps.get_model(app_config.label,model_name)
            break
        except LookupError:
            continue
    if not models:
        print("Model not found")
    return models.__name__

print(get_model_config('Licence_Keys'))