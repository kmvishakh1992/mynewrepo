from __future__ import unicode_literals
from django.shortcuts import render
from .forms import PostForm

# Create your views here.
"""
Views which allow users to create and activate accounts.

"""

from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.utils.decorators import method_decorator
from django.utils.module_loading import import_string
from django.views.decorators.debug import sensitive_post_parameters

import os
from django.shortcuts import render_to_response
from django.http import Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.encoding import smart_text
from wsd.lesk import adapted_lesk



def index(request):
	return render(request, 'myapp/hello.html')
def act(request):
	if request.method == 'POST' and (request.POST.get('amb')=="submit"):
		text=""
		text = request.POST.get('sent')

		amb = request.POST.get('wsd')
		answer = adapted_lesk(text, amb, pos='n')
		defi = answer.definition()
		return render(request,'myapp/hello.html', {'defi': defi,'text' : text, 'amb' : amb})
		#return render(request,'myapp/hello.html', {'answer': answer},content_type="text/plain")
    	#return HttpResponse("Hello, world. You're at the polls index.")		#return render(request,'myapp/hello.html',{'form': form}, {'defi': defi,'text' : text, 'amb' : amb})

		#return HttpResponse({'answernn' : answer})

def show_hello(request):
	return render(request,'myapp/hello.html')

def post_new(request):
    form = PostForm()
    return render(request, 'myapp/extend.html', {'form': form})
  



