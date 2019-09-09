from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
#from django.template import loader

# Create your views here.


"""
# Crea una vista que regresa un HTML(Template)
def index(request):
    return render(request, 'Home/index.html')
"""

"""
# Function views
def index(request):
   
    '''
       Index in my Web Page.
    '''
    print(request.method)
    template = 'Home/index.html'
    context = {}
    return render(request, template, comtext)

"""

# Class-based Views
class Index(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/index.html'
    context = {'title': 'Index'}

    def get(self, request):
        """
            Get in my Index.
        """
        print('With class-based views')
        return render(request, self.template, self.context)


class About(View):
    """
        About me page.
    """
    template = 'Home/about.html'
    context = {'title': 'About me'}

    def get(self, request):
        """
            Get in About me.
        """
        return render(request, self.template, self.context)
