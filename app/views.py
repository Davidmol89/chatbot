from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout
from django.conf import settings

# Este diccionario simulará una "base de datos" mínima para usuarios
# o podrías usar el sistema de usuarios de Django.
# En un proyecto real, lo ideal es verificar el token con Firebase Admin SDK
# y manejar usuarios en la BD. Aquí simplificamos.
SESSION_KEY_USER = 'usuario_actual'

def inicio_view(request):
    return render(request, 'inicio.html')

def login_view(request):
    # Si ya está autenticado en sesión, redirige a home
    if SESSION_KEY_USER in request.session:
        return redirect('home')
    return render(request, 'login.html')

def firebase_auth(request):
    """
    Esta vista recibe un POST con la info del usuario proveniente de Firebase.
    Verificamos el dominio y guardamos la sesión.
    """
    if request.method == 'POST':
        user_data = request.POST
        email = user_data.get('email')
        name = user_data.get('name')
        photo = user_data.get('photo')

        # Verificamos que el dominio sea @umariana.edu.co
        if email.endswith('@umariana.edu.co'):
            # Guardamos los datos en la sesión
            request.session[SESSION_KEY_USER] = {
                'name': name,
                'email': email,
                'photo': photo
            }
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Dominio no permitido'})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'})

def home_view(request):
    # Verificar si el usuario está en sesión
    user = request.session.get(SESSION_KEY_USER, None)
    if not user:
        return redirect('login')
    return render(request, 'home.html', {'user': user})

def logout_view(request):
    # Cerrar sesión
    if SESSION_KEY_USER in request.session:
        del request.session[SESSION_KEY_USER]
    logout(request)
    return redirect('login')
