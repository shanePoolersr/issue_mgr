from django.views.genric import (
CreateView,
DetailView,
UpdateView,
DeleteView,
ListView
)
from django.urls
from .models import  Issue

# Create your views here.
class IssueCreateView(CreateView)
 template_name = "issues/new,html"