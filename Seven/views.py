from django.views.generic import TemplateView
from django.http import FileResponse
from django.views import View
import os

# TemplateViews for rendering HTML templates
class SevenHome(TemplateView):
    template_name = "Class/Seven/Code/Seven_Math.html"

class OneView(TemplateView):
    template_name = "Class/Seven/Section One/Seven.html"

class TwoView(TemplateView):
    template_name = "Class/Seven/Section Two/Seven.html"

class ThreeView(TemplateView):
    template_name = "Class/Seven/Section Three/Seven.html"

class FourView(TemplateView):
    template_name = "Class/Seven/Section Fore/Seven.html"

class FiveView(TemplateView):
    template_name = "Class/Seven/Section Five/Seven.html"

class SixView(TemplateView):
    template_name = "Class/Seven/Section Six/Seven.html"

class SevenView(TemplateView):
    template_name = "Class/Seven/Section Seven/Seven.html"

class EightView(TemplateView):
    template_name = "Class/Seven/Section Eight/Seven.html"

class NineView(TemplateView):
    template_name = "Class/Seven/Section Nine/Seven.html"

# View classes for downloading PDF files
class Download_One(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Seven', 'One.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='One.pdf')

class Download_Two(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Seven', 'Two.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Two.pdf')

class Download_Three(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Seven', 'Three.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Three.pdf')

class Download_Four(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Seven', 'Fore.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Fore.pdf')

class Download_Five(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Seven', 'Five.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Five.pdf')

class Download_Six(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Seven', 'Six.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Six.pdf')

class Download_Seven(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Seven', 'Seven.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Seven.pdf')

class Download_Eight(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Seven', 'Eight.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Eight.pdf')

class Download_Nine(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Seven', 'Nine.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Nine.pdf')
    
