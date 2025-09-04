from django.shortcuts import render

# Create your views here.

def general_info(request):
    return render(request, 'mainapp/general_info.html')

def inicio(request):
    return render(request, 'mainapp/inicio.html')

def nosotros(request):
    return render(request, 'mainapp/nosotros.html')

def servicios(request):
    return render(request, 'mainapp/servicios.html')

def contactanos(request):
    return render(request, 'mainapp/contactanos.html')


def contactanos_2(request):
    from .forms import ContactForm
    from django.shortcuts import redirect
    from django.contrib import messages
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('mainapp:contactanos_2')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'mainapp/contactanos_2.html', {'form': form})


def enlaces(request):
    return render(request, 'mainapp/enlaces.html')


def equipo(request):              
    return render(request, 'mainapp/equipo.html')

from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the form data to the database
            return redirect('post_list')  # Redirect to a list of posts
    else:
        form = PostForm ()
    return render(request, 'create_post.html', {'form': form})


from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})



