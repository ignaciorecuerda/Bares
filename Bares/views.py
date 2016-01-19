# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from Bares.models import Bar, Tapa
from Bares.forms import UserForm, UserProfileForm, BarForm, TapaForm
from django.template.defaultfilters import slugify
from django.http import JsonResponse
from django.core import serializers
import json


def index(request):
    lista_bares = Bar.objects.order_by('nombre')
    lista_tapas = Tapa.objects.order_by('titulo')
    # lista_tapas = Tapa.objects.filter(nombrebar=Bar.nombre)
    # context_dict = {'bares':lista_bares}
    context_dict = {'bares':lista_bares, 'tapas': lista_tapas}
    return render(request, 'Bares/Cuerpo.html', context_dict)


# def tapas(request):
#     context_dict = {}
#     lista_tapas = Tapa.objects.order_by('titulo')
#     # lista_tapas = Tapa.objects.filter('nombrebar')
#     context_dict = {'tapas':lista_tapas}
#     return render(request, 'Bares/tapas.html', context_dict)


def about(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'Bares/about.html', context_dict)
    # ese base.html será la base de todas las páginas web. aquí estamos en el views de Bares.
    # Por tanto aquí llamaremos a /bares/base.html y es ese base.html el que llamará al base de todas las apps

def register(request):
     # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'Bares/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



# @logout_required
def user_login(request):
 # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/Bares/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'Bares/login.html', {})


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/Bares/')


def bar(request, bar_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    lista_bares = Bar.objects.order_by('nombre')
    context_dict = {'bares':lista_bares}
    bar = Bar.objects.get(slug = bar_name_slug)
    print bar.nombre
    print "LOGO DEL BAR" + bar.logo.name
    if bar:
        context_dict['bar'] = bar
        bar.visitas += 1
        bar.save()
        tapas = Tapa.objects.filter(nombrebar = bar)
        context_dict['tapas'] = tapas
#    else:
#        context_dict['bar_name'] = "ningun bar"
    return render(request, 'Bares/bar.html', context_dict)


@login_required
def add_bar(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = BarForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = BarForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'Bares/add_bar.html', {'form': form})


#def add_tapa(request, bar_name_slug):
#    context_dict = {}
#    print "hola"
#    if request.method == 'POST':
#        bar = Bar.objects.get(nombre = bar_name_slug)
#        if bar:
#            
#            tapas = Tapa.objects.filter(nombrebar = bar)
#            form = TapaForm(request.POST)
#            if form.is_valid():
#                if tapas:
#                    tapas = form.save(commit=False)
#                    tapa.nombrebar = bar.nombre
#                    tapa.save()
#                    # probably better to use a redirect here.
#                    return Bar(request, bar_name_slug)
#            else:
#                print form.errors
#            context_dict = {'form':form, 'bar': bar}
#    else:
#        form = TapaForm()
#    return render(request, 'Bares/add_tapa.html', context_dict)



def add_tapa(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = TapaForm(request.POST, request.FILES)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = TapaForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'Bares/add_tapa.html', {'form': form})


def visitas(request):
    # A HTTP POST?
    
    return render(request, 'Bares/visitas.html')


def reclama_datos(request):
    bares = Bar.objects.order_by('nombre')
    data = serializers.serialize('json', bares, fields=('nombre', 'visitas'))
    response = []
    for bar in bares:
        response.append(bar.nombre)
        response.append(bar.visitas)
    return HttpResponse(json.dumps(response), content_type="application/json")    
#    print bares
#    return HttpResponse(bares) 
#    return JsonResponse(bares, safe=False)
#    return HttpResponse(data, mimetype='application/json')
#    return JsonResponse(datos, safe=False)


def megusta_tapa(request):
    titulotapaclickada = request.GET['titulo']
    bar = request.GET['bar']
    print "has clickado en la tapa" + titulotapaclickada + " que es del bar " + bar
    tapas = Tapa.objects.filter(titulo = titulotapaclickada, nombrebar__slug = bar) #solo va a devolver una, pero no puedo hacer tapas.megustas: AttributeError: 'QuerySet' object has no attribute 'megustas'. haciendo casting me da 0. hago un bucle for e ya.
    for tapa in tapas:
        tapa.megustas +=1
        tapa.save()
    return HttpResponse("Your Rango account is disabled.")
    


