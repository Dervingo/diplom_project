from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse
from django.core.paginator import Paginator
from .models import Diplom
from .forms import DiplomForm

MAX_DIPLOM_ON_PAGE = 5

# def index(request):
#     return HttpResponse('Диплом ПОКАЖИ!!!!!')


def index(request):
    diploms = Diplom.objects.all()
    paginator = Paginator(diploms, MAX_DIPLOM_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'diploms': diploms,
        'page_obj': page_obj,
    }
    return render(request, 'diplom/diplom_list.html', context)


def diplom_edit(request, pk):
    diplom = get_object_or_404(Diplom, pk=pk)
    if request.method == 'POST':
        form = DiplomForm(request.POST or None, files=request.FILES or None,
                          instance=diplom)
        if form.is_valid():
            form.save()
            return redirect(reverse('diplom_spo:index'))
    else:
        form = DiplomForm(instance=diplom)
    return render(request, 'includes/diplom_form.html', {'form': form})


def diplom_detail(request, pk):
    diplom = get_object_or_404(Diplom, pk=pk)
    context = {
        'diplom': diplom
    }
    return render(request, 'diplom/diplom_detail.html', context)


def diplom_create(request):
    if request.method == 'POST':
        form = DiplomForm(request.POST or None, files=request.FILES or None,)
        if form.is_valid():
            form.save()
            return redirect(reverse('diplom_spo:index'))
    else:
        form = DiplomForm()
    return render(request, 'includes/diplom_form.html', {'form': form})


# def diplom_create(request):
#     form = DiplomForm(
#         request.POST or None,
#         files=request.FILES or None
#     )
#     if form.is_valid():
#         form.save()  # сохраняем паспорт в базу данных
#         return redirect(reverse('diplom:index'))  # перенаправляем на главную страницу
#     return render(request, 'diplom/diplom_create.html', {'form': form})
