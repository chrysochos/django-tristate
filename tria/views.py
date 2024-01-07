
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from tria.models import MyModel
from django.views.generic.edit import FormView
from django import forms
from django.utils.safestring import mark_safe
from .models import MyModel
from tri.forms import TriStateField

def my_view(request):
    # Fetch the latest instance of MyModel
    latest_instance = MyModel.objects.order_by('-id').first()

    if request.method == 'POST':
        form = MyForm(request.POST, instance=latest_instance)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('../form/')  # Redirect to a success URL
    else:
        # Initialize the form with the latest instance
        form = MyForm(instance=latest_instance)

    return render(request, 'form_template.html', {'form': form})

# Form Definition
class MyForm(forms.ModelForm):
    my_tri_state_field1 = TriStateField(label='Field 1')
    my_tri_state_field2 = TriStateField(label='Field 2')
    # Add more fields as needed

    class Meta:
        model = MyModel
        fields = ['my_tri_state_field1', 'my_tri_state_field2']

# View
class MyFormView(FormView):
    template_name = 'form_template.html'
    form_class = MyForm
    success_url = '/success/'

    def form_valid(self, form):
        # Process the data in form.cleaned_data
        return super().form_valid(form)