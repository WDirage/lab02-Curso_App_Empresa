from math import pi
from django.shortcuts import render


def index(request):
    context = {'titulo': 'Formulario'}
    return render(request, 'encuesta/formulario.html', context)


def enviar(request):
    if request.method != 'POST':
        return render(request, 'encuesta/formulario.html', {'titulo': 'Formulario'})
    context = {
        'titulo': 'Respuesta',
        'nombre': request.POST.get('nombre', ''),
        'clave': request.POST.get('password', ''),
        'educacion': request.POST.get('educacion', ''),
        'nacionalidad': request.POST.get('nacionalidad', ''),
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST.get('email', ''),
        'website': request.POST.get('sitioweb', ''),
    }
    return render(request, 'encuesta/respuesta.html', context)


def operaciones(request):
    resultado = None
    error = None
    if request.method == 'POST':
        try:
            a = float(request.POST.get('numero1', ''))
            b = float(request.POST.get('numero2', ''))
            operacion = request.POST.get('operacion', 'suma')
            if operacion == 'suma':
                resultado = a + b
                simbolo = '+'
            elif operacion == 'resta':
                resultado = a - b
                simbolo = '−'
            elif operacion == 'multiplicacion':
                resultado = a * b
                simbolo = '×'
            else:
                raise ValueError('Selecciona una operación válida.')
            resultado = {'numero1': a, 'numero2': b, 'valor': resultado,
                         'operacion': operacion, 'simbolo': simbolo}
        except (TypeError, ValueError):
            error = 'Introduce dos números válidos y selecciona una operación.'
    return render(request, 'encuesta/operaciones.html',
                  {'resultado': resultado, 'error': error})


def cilindro(request):
    resultado = None
    error = None
    if request.method == 'POST':
        try:
            diametro = float(request.POST.get('diametro', ''))
            altura = float(request.POST.get('altura', ''))
            if diametro <= 0 or altura <= 0:
                raise ValueError
            radio = diametro / 2
            volumen = pi * radio ** 2 * altura
            resultado = {'diametro': diametro, 'altura': altura, 'volumen': volumen}
        except (TypeError, ValueError):
            error = 'Introduce un diámetro y una altura válidos, mayores que cero.'
    return render(request, 'encuesta/cilindro.html',
                  {'resultado': resultado, 'error': error})
