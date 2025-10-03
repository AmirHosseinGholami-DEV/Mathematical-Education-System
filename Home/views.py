from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

# LoginView class to handle login operations
class LoginView:
    def get(self, request):
        # Render the login page on GET request
        return render(request, 'login.html')

    def post(self, request):
        # Process login on POST request
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If user is authenticated, log them in and redirect to home page
            login(request, user)
            return redirect('home')
        else:
            # If authentication fails, show error message and render login page again
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است!')
            return render(request, 'login.html')

    def handle_request(self, request):
        # Handle the request based on its method (GET or POST)
        if request.method == 'POST':
            return self.post(request)
        return self.get(request)

# Function-based view for login
def login_view(request):
    view = LoginView()
    return view.handle_request(request)

# LogoutView class to handle logout operations
class LogoutView:
    def get(self, request):
        # Log the user out and show a success message
        logout(request)
        messages.success(request, 'شما با موفقیت خارج شدید!')
        return redirect('home')

    def handle_request(self, request):
        # Handle the logout request (only GET method)
        return self.get(request)

# Function-based view for logout
def logout_view(request):
    view = LogoutView()
    return view.handle_request(request)

# SignUpView class to handle user registration
class SignUpView(FormView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Save the new user
        user = form.save()
        
        # Authenticate and login the user
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'حساب کاربری با موفقیت ایجاد شد!')
            return super().form_valid(form)
        else:
            return redirect('register')

    def form_invalid(self, form):
        # Handle specific field errors
        for field, errors in form.errors.items():
            for error in errors:
                if field == 'username':
                    if 'required' in error.lower():
                        messages.error(self.request, 'نام کاربری الزامی است.')
                    elif 'exists' in error.lower():
                        messages.error(self.request, 'این نام کاربری قبلاً استفاده شده است.')
                elif field == 'password1':
                    if 'short' in error.lower():
                        messages.error(self.request, 'رمز عبور باید حداقل ۸ کاراکتر باشد.')
                    elif 'common' in error.lower():
                        messages.error(self.request, 'رمز عبور بسیار ساده است.')
                    elif 'numeric' in error.lower():
                        messages.error(self.request, 'رمز عبور نمی‌تواند فقط عدد باشد.')
                elif field == 'password2':
                    if 'match' in error.lower():
                        messages.error(self.request, 'رمزهای عبور مطابقت ندارند.')
        
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context
# TemplateView classes for rendering various pages
class HomeView(TemplateView):
    template_name = "home.html"

class VideoView(TemplateView):
    template_name = "Movies.html"

class AboutView(TemplateView):
    template_name = "about.html"

class AiView(TemplateView):
    template_name = "ai.html"

class EducationView(TemplateView):
    template_name = "education system.html"

class RegisterView(TemplateView):
    template_name = "register.html"

class StemView(TemplateView):
    template_name = "stem.html"
