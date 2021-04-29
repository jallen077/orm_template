# Django specific settings 

import inspect 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","settings")

from django.db import connection

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
from standalone.models import Test

# Delete all data
def clean_data():
    Test.objects.all().delete()

# Test Django Model Setup
def test_setup():
    try:
        clean_data()
        test = Test(name="name")
        test.save()
        # Check that the table is not empty
        assert Test.object.count() > 0
        print("Django Model setup complete.")
    except AssertionError as exception:
        print("Django Model setup failed with error: ")
        raise(exception)
    except:
        print("Unexpected Error")

test_setup()


