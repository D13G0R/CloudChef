from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import request
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from restaurante import settings
from .models import Users, Restaurantes
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from aplicaciones.users.forms import registerForm, loginForm, formAddUser, registerEnterprise


class index(LoginRequiredMixin, ListView):
    model = Users
    template_name = "index.html"

    # def get_queryset(self):
    #     return Users.objects.filter(fk_id_rol_id__lte=1) el query set es para modificar o persoanlizar la consulta
    # y no solo mostrarlos todos

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        Users.objects.filter(fk_restaurante_id = self.request.session.get("restaurante"))
        contexto["titulo"] = "Inicio"
        return contexto

#La idea sería que cuando se registren ya tenga la id del restaurante desde el QR.
class register(CreateView):
    form_class = registerForm
    template_name="register.html"
    success_url = reverse_lazy("loginUser")

    #Sobreescribimos para poder hashear la contraseña con Argon2 manualmente (No hace falta pero es para practicar)
    def form_valid(self, form):
        user = form.save(commit = False)
        user.set_password(form.cleaned_data["password1"])
        user.save()
        return super().form_valid(form)


class loginUser(View):  # Use PascalCase for class names
    form_class = loginForm
    template_name = "login.html"

    def get(self, request):
        form = self.form_class()  # Instantiate the form
        return render(request, self.template_name, {"form": form})

    def post(self, request):
                                                                                        # print("POST data:", request.POST) DEBUG
        form = self.form_class(request, data=request.POST)
                                                                                        # print("antes de la validacion del formulario") DEBUG

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
                                                                                        # print(f"Despues")DEBUG
            if user is not None:
                # Check if the user has a valid fk_restaurante_id
                if hasattr(user, 'fk_restaurante_id'):
                    restaurante = user.fk_restaurante_id
                    request.session["restaurante"] = restaurante
                    print(restaurante)
                else:
                    # Handle the case where fk_restaurante_id is missing
                    form.add_error(None, "El usuario no está asociado a un restaurante.")
                    return render(request, self.template_name, {"form": form})

                # Log the user in
                login(request, user)
                return redirect("home")
            else:
                # Authentication failed
                form.add_error(None, "Nombre de usuario o contraseña incorrecta")
        else:
            # Print form errors to debug
            print("Form errors:", form.errors)

        # If the form is invalid or authentication fails, re-render the form with errors
        return render(request, self.template_name, {"form": form})

def Signout(request):
    logout(request)  # Cierra la sesión
    return redirect('loginUser')  # Redirige a la página de loginUser


class registerEnterprise (CreateView):
    model = Restaurantes
    template_name = "registerEnterprise.html"
    form_class = registerEnterprise
    success_url = reverse_lazy("register")


class addUser(CreateView):
    model = Users
    template_name = "formularioAgregarUsuario.html"
    success_url = reverse_lazy("adminUsers")
    form_class = registerForm

class editUser(UpdateView):
    model = Users
    template_name = "formularioEditarUsuario.html"
    success_url = reverse_lazy("adminUsers")
    form_class = formAddUser

class deleteUser(DeleteView):
    model = Users
    template_name = "confirmDeleteUser.html"
    success_url = reverse_lazy("adminUsers")

