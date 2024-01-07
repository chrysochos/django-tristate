# Django Tri-State Module

Django Tri-State Module provides a custom form field and widget for handling tri-state data (True, False, None) using two checkboxes in Django forms.

## Installation

First, install the module via pip (assuming you have packaged and distributed it, for example on PyPI):

    pip install django-tristate
Alternatively, if the module is not on PyPI, you can install it directly from a GitHub repository (replace url-to-repo with the actual URL):

    pip install git+url-to-repo
Or, if you have the module locally:

    pip install path/to/django-tristate

## Configuration
After installation, add django_tristate to your INSTALLED_APPS in your Django settings:

    INSTALLED_APPS = [
        # ... Other installed apps ...
        'django_tristate',
    ]

## Usage
### In Forms
    Import TriStateField from the module and use it in your forms:

    from django import forms
    from django_tristate.forms import TriStateField

    class ExampleForm(forms.Form):
        my_tri_state_field = TriStateField()
### In Models
If you wish to use the tri-state logic with Django models, define a model field with null=True:

    from django.db import models

    class ExampleModel(models.Model):
        my_tri_state_field = models.BooleanField(null=True, blank=True)
Then use ExampleForm in your views as you would with a standard Django form.

### In Templates
Render the form in your templates:

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
JavaScript logic for the tri-state behavior should be included in the template where the form is rendered.

## Customization
You can customize the TriStateField behavior by overriding its methods or extending the TriStateWidget. Refer to the Django documentation on creating custom form fields for more details.

## Contributing
Your contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing
The code in this project is licensed under MIT license.

This README provides a comprehensive guide for users on how to install, configure, and use your Django tri-state module. You can adjust the content as necessary to fit the specifics of your module and your GitHub repository details.





