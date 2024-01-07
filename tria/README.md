# Tria App

The `tria` app is a part of the `tristate_example` Django project. It provides specific functionalities, integrating the generic tri-state logic provided by the `tri` module.

## Setup

To use `tria` in your Django project:

1. Ensure `tri` is installed and configured in your project.

2. Add `tria` to your `INSTALLED_APPS` in `settings.py`:

   ```python
   INSTALLED_APPS = [
       # ... other installed apps ...
       'tria',
   ]
    ```
Include tria's URLs in your project's urls.py:

    from django.urls import include, path

    urlpatterns = [
        # ... other url patterns ...
        path('tria/', include('tria.urls')),
    ]

## Usage
### Views
tria provides the following views:

ExampleView: Shows how to use the tri-state field in a form.
## Forms
Use TriStateField from the tri module in your forms as follows:

    from django import forms
    from tri.forms import TriStateField

    class ExampleForm(forms.Form):
        example_field = TriStateField()

## Models
If you have models using the tri-state logic, define them as follows:

    from django.db import models

    class ExampleModel(models.Model):
        example_field = models.BooleanField(null=True, blank=True)

## Migrations

If you have made changes to the models in `tria` or are using it for the first time, you'll need to create and apply migrations. Migrations are how Django propagates changes you make to your models (adding a field, deleting a model, etc.) into the database schema.

If you like to use sqlite3, configure your database settings in `settings.py` as follows:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

To create and apply migrations for `tria`, follow these steps:

1. **Create Migrations**: Run the following command to create migration files for `tria`. This command tells Django to prepare the changes you've made to your models for the database:

   ```bash
   python manage.py makemigrations tria

2. **Apply Migrations**: After creating the migrations, apply them to update the database schema:

    python manage.py migrate tria

Remember to run these commands from the same directory where your manage.py file is located.


## Customizing tria
You can extend the views or forms provided by tria by subclassing them.
For more complex customizations, you may modify the source code directly.
## Dependencies
tria depends on the tri module for the tri-state form field functionality.


### Conclusion

Your application will be like `tria` app. So, you must study it in order to see how to use django-tristate.

## Resources

