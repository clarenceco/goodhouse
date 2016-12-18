# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Post
from .forms import DocumentForm


# Create your views here.


def HomePageView(request):
	context = {}
	return render(request, 'base.html', context)



# def list(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile = request.FILES['docfile'])
#             newdoc.save()

#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('homepageview'))
#             #return render(request, 'base.html', {})
#     else:
#         form = DocumentForm() # A empty, unbound form

#     # Load documents for the list page
#     documents = Document.objects.all()

#     # Render list page with the documents and the form
#     return render(request, 'gh_app/list.html', {'documents': documents, 'form': form})


