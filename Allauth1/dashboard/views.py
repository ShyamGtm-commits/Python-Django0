from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account import app_settings

class CustomSignupView(SignupView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = "Join me using our cutting-edge,AI-powered, blockchain enabled, cloud-native platforms to disrupt the paradigm and synersize the exponential growth "
        
    def form_valid(self, form):
        response = super().form_valid(form)

        if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
            messages.info(
                self.request,
                "We have sent you an verification mail to verify your account. Please Check your inbox."

            )
        else:
            messages.success(
                self.request,
                f"Welcome {form.cleaned_data['first_name']}! Your account has been created."
            )
# Create your views here.


def profile(request):
    return render(request, 'profile.html')