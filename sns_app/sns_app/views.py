from django.http import JsonResponse


def base_view(request):
    return JsonResponse({"data": "YOU ARE HERE"})
