from django.http import HttpResponse
# simplest view possible in Django
def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
