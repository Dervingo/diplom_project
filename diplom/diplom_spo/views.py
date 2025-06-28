from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Diplom
from .forms import DiplomForm
from django.urls.base import reverse


def index(request):
    return HttpResponse('Диплом ПОКАЖИ!!!!!')


def diplom_list(request):
    diploms = Diplom.objects.all()
    return render(request, 'diplom/diplom_list.html', {'diploms': diploms})


def diplom_edit(request, pk):
    diplom = get_object_or_404(Diplom, pk=pk)
    if request.method == 'POST':
        form = DiplomForm(request.POST, instance=diplom)
        if form.is_valid():
            form.save()
            return redirect('diplom_list')
    else:
        form = DiplomForm(instance=diplom)
    return render(request, 'diplom/diplom_form.html', {'form': form})


def diplom_create(request):
    if request.method == 'POST':
        form = DiplomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diplom_list')
    else:
        form = DiplomForm()
    return render(request, 'diplom/diplom_form.html', {'form': form})


# def diplom_create(request):
#     form = DiplomForm(
#         request.POST or None,
#         files=request.FILES or None
#     )
#     if form.is_valid():
#         form.save()  # сохраняем паспорт в базу данных
#         return redirect(reverse('diplom:index'))  # перенаправляем на главную страницу
#     return render(request, 'diplom/diplom_create.html', {'form': form})

