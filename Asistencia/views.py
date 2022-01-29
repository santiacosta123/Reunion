from django.shortcuts import redirect, render
from .models import Lider, Persona

# Create your views here.
def home(request):
  personasListado = Persona.objects.all()
  return render(request, "registro_usuarios.html", {"personas" : personasListado})


def registrarUsuario(request):
  cedula = request.POST['txtCedula']
  nombre_completo = request.POST['txtNombreCompleto']
  telefono = request.POST['txtTelefono']
  lider_referido = request.POST['txtLiderReferido']

  usuario = Persona.objects.create(
    cedula = cedula, nombre_completo = nombre_completo, telefono = telefono, lider_referido = lider_referido
  )

  return redirect('/')

  