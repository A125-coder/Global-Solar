from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             print('Вітаємо! Ви залогінились')
#             return redirect("dashboard")
#         else:
#             print("Невірний логін або пароль")
#             return redirect('login')

#     else:
#         return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['surname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Користувач з таким ім"ям вже існує')
                return redirect('register')
            else: 
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Такие емейл вже існує')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username = username,
                        password= password,
                        email = email,
                        first_name = first_name,
                        last_name = last_name
                    )
                    user.save()
                    messages.success(request, 'Ви успішно зареєструвались!')
                    return redirect('dashboard')

        else:
            messages.error(request, "Паролі не співпадають!")
            return redirect('register')

            

    return render(request, 'accounts/register.html')




def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect(request, "pages/home.html")