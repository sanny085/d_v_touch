from django.http import JsonResponse

def hello_touch(request): 
    return JsonResponse({'message': 'Hello, touch!'})
