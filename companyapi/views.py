from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        "Himanshu",
        "Manjeet",
        "Dhruv",
        "Aryan",
        "pranjal"
    ]
    return JsonResponse(friends, safe=False)