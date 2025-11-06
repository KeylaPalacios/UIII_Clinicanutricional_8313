from django.shortcuts import render, redirect, get_object_or_404
from .models import Nutriologo

# Página de inicio
def inicio_clinicanutricional(request):
    return render(request, 'inicio.html')

# Agregar nutriólogo
def agregar_nutriologo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        experiencia = request.POST.get('experiencia')
        especialidad = request.POST.get('especialidad')

        nuevo = Nutriologo(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            direccion=direccion,
            telefono=telefono,
            experiencia=experiencia,
            especialidad=especialidad
        )
        nuevo.save()
        return redirect('ver_nutriologos')

    return render(request, 'nutriologos/agregar_nutriologo.html')

# Ver nutriólogos
def ver_nutriologos(request):
    nutris = Nutriologo.objects.all()
    return render(request, 'nutriologos/ver_nutriologos.html', {'nutris': nutris})

# Actualizar nutriólogo (formulario de edición)
def actualizar_nutriologo(request, id):
    nutri = get_object_or_404(Nutriologo, pk=id)
    return render(request, 'nutriologos/actualizar_nutriologo.html', {'nutri': nutri})

# Realizar actualización
def realizar_actualizacion_nutriologo(request, id):
    nutri = get_object_or_404(Nutriologo, pk=id)
    if request.method == 'POST':
        nutri.nombre = request.POST.get('nombre')
        nutri.apellido = request.POST.get('apellido')
        nutri.correo = request.POST.get('correo')
        nutri.direccion = request.POST.get('direccion')
        nutri.telefono = request.POST.get('telefono')
        nutri.experiencia = request.POST.get('experiencia')
        nutri.especialidad = request.POST.get('especialidad')
        nutri.save()
        return redirect('ver_nutriologos')
    return redirect('ver_nutriologos')

# Borrar nutriólogo
def borrar_nutriologo(request, id):
    nutri = get_object_or_404(Nutriologo, pk=id)
    if request.method == 'POST':
        nutri.delete()
        return redirect('ver_nutriologos')
    return render(request, 'nutriologos/borrar_nutriologo.html', {'nutri': nutri})