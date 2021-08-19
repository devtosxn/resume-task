from django.shortcuts import render, redirect


def home(request):
    if request.method == 'POST':
        return redirect('contact')
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'contact.html', {})