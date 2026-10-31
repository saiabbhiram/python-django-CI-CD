from django.shortcuts import render
from django.http import JsonResponse
from .models import Item


def index_view(request):
    items = Item.objects.all().order_by('-created_at')
    context = {
        'items': items,
        'title': 'Django & Jenkins Freestyle CI Demo',
        'status': 'Operational',
    }
    return render(request, 'demo_app/index.html', context)


def health_check_view(request):
    """Simple JSON healthcheck endpoint for CI smoke tests / probes."""
    return JsonResponse({
        'status': 'ok',
        'service': 'django-jenkins-demo',
        'database_connected': True,
    })
