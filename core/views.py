
from django.shortcuts import redirect, render

# Create your views here.


def api(request):
    return redirect('public')


def public(request):
    return render(request, 'public.html', {})
