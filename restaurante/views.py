from django.shortcuts import render

def home (request):

    contexto = {
        "mensaje": "Bienvenido"
    }
    return render( request, "home.html", contexto)

def presentacion(request):
    return render(request, "inicio.html")