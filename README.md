# Django Tri-State Module

Brief introduction to the module and its functionality.

## Installation

Instructions on how to install the `tri` module. 

```bash
pip install django-tristate  # It is available via PyPI
```

## Configuration

  # settings.py
  INSTALLED_APPS = [
      ...
      'tri',
  ]


## Usage
In github repository of django-tristate, there is a folder called `tristate_example`. It contains a Django project example called `tristate_example` and an app called `tria`. The `tria` app is a part of the `tristate_example` Django project. It provides specific functionalities, integrating the generic tri-state logic provided by the `tri` app/module.

In tria app you can find the following:
    views.py: Shows how to use the tri-state field in a form. It has the forms and views for the example.
    models.py: Shows how to use the tri-state field in a model. It has the models for the example.
    urls.py: Shows how to use the tri-state field in a form. It has the urls for the example. Have in mind that the urls are included in the project's urls.py. So, you need to use /tria/form url to access the example.

Forms are in the views.py file.

In templates folder you will see the form_template.html file which is the template for the form. It has a JavaScript logic for the tri-state behavior. When you click on the checkboxes, the JavaScript logic is triggered to see if you have click on both checkboxes and turn off the other one checkbox. 
With the Submit button, the state of the checkboxes is saved and with GET you get the last saved state in the form.

## Contact
Ioannis Chrysochos
ioannis.chrysochos@cytanet.com.cy

## Example
You can use the whole project as an example

## Contact
Ioannis Chrysochos
ioannis.chrysochos@cytanet.com.cy

