from django.views.generic import TemplateView
from django.http import FileResponse
from django.views import View
import os

# TemplateViews for rendering HTML templates
class NineHome(TemplateView):
    template_name = "Class/Nine/Code/Nine_Math.html"

class OneView(TemplateView):
    template_name = "Class/Nine/Section One/Seven.html"

class TwoView(TemplateView):
    template_name = "Class/Nine/Section Two/Seven.html"

class ThreeView(TemplateView):
    template_name = "Class/Nine/Section Three/Seven.html"

class FourView(TemplateView):
    template_name = "Class/Nine/Section Fore/Seven.html"

class FiveView(TemplateView):
    template_name = "Class/Nine/Section Five/Seven.html"

class SixView(TemplateView):
    template_name = "Class/Nine/Section Six/Seven.html"

class SevenView(TemplateView):
    template_name = "Class/Nine/Section Seven/Seven.html"

class EightView(TemplateView):
    template_name = "Class/Nine/Section Eight/Seven.html"

class NineView(TemplateView):
    template_name = "Class/Nine/Section Nine/Seven.html"

# View classes for downloading PDF files
class Download_One(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Nine', 'One.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='One.pdf')

class Download_Two(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Nine', 'Two.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Two.pdf')

class Download_Three(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Nine', 'Three.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Three.pdf')

class Download_Four(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Nine', 'Four.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Four.pdf')

class Download_Five(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Nine', 'Five.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Five.pdf')

class Download_Six(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Nine', 'Six.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Six.pdf')

class Download_Seven(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Nine', 'Seven.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Seven.pdf')

class Download_Eight(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Nine', 'Eight.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Eight.pdf')

class Download_Nine(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join('media', 'Nine', 'Nine.pdf')
        return FileResponse(open(file_path, 'rb'), 
            content_type='application/pdf', as_attachment=True, filename='Nine.pdf')

