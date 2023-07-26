from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _

from django.contrib.auth import authenticate, login


class LoginController:
    def __init__(self, request):
        self.request = request
        self.username = None
        self.password = None
        self.error = None
        self.user = None

    def handle_request(self):
        ok = 0
        if self.request.method == 'POST':
            form = AuthenticationForm(data=self.request.POST)
            if form.is_valid():
                self.username = form.cleaned_data.get('username')
                self.password = form.cleaned_data.get('password')
                self.user = authenticate(request=self.request, username=self.username, password=self.password)
                if self.user is not None:
                    login(self.request, self.user)
                    if self.user.is_employee:
                        ok = 1
                    if self.user.is_manager:
                        ok = 2
                    if self.user.is_admin:
                        ok = 3
        context = {'form': AuthenticationForm(),
                   'Login':_('Login')}
        return ok, context
