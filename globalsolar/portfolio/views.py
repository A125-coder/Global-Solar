from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Portfolio
# Create your views here.


def index(request):
    our_works = Portfolio.objects.order_by(
        '-voltage').filter(is_published=True)
    paginator = Paginator(our_works, 4)
    page = request.GET.get('page')
    pagged_works = paginator.get_page(page)
    context = {
        'our_works': pagged_works
    }
    return render(request, "pages/our_works.html", context)


def work(request, work_id):
    work = get_object_or_404(Portfolio, pk=work_id)
    context = {
        'work': work
    }
    return render(request, 'pages/one_work.html', context)
