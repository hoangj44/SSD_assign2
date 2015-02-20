#views.py
from secSoftwareA2.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


#from .models import ModelWithFileField
 
@csrf_protect
def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = User.objects.create_user(
      username=form.cleaned_data['username'],
      password=form.cleaned_data['pass_wd'],
      email=form.cleaned_data['email']
      )
      return HttpResponseRedirect('/register/success/')
  else:
    form = RegistrationForm()
  variables = RequestContext(request, {
  'form': form
  })
  return render_to_response(
  'registration/register.html',
  variables,
  )
 
def register_success(request):
  return render_to_response('registration/success.html',
  )


  
def update_success(request):
  return render_to_responce('registration/updateSuccess.html',
  )

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')
  
@csrf_protect
def update(request):
  if request.method == 'POST':
    form = UpdateForm(data=request.POST, instance=request.user)
    if form.is_valid():
      return HttpResponseRedirect('/register/updatesuccess/')
  else:
    form = UpdateForm()
    variables = RequestContext(request, {
    'form': form
    })
  return render_to_response(
  'registration/update.html',
  variables,
  )

@login_required
def home(request):
  return render_to_response(
  'home.html',
  { 'user': request.user }
  )

#@login_required  
#def change_passwd(request):
  #form = PasswordChangeForm(user=request.user)
  #if form.is_valid():
    #form.save()
    #update_session_auth_hash(request, form.user)
  #else:
    #return render(request, 'registration/password_change_form.html', {
        #'form': form,
    #})
  
  
  #if request.method == 'POST':
    #form = PasswordChangeForm(user=request.user, data=request.POST)
    #if form.is_valid():
      #form.save()
      #update_session_auth_hash(request, form.user)
  #else:
    #form = UpdateForm()
    #variables = RequestContext(request, {
    #'form': form
    #})
    
  #return render_to_response(
  #'registration/password_change_form.html',
  #variables,
  #)
