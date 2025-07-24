from django.shortcuts import render

# Create your views here.
def homepage(request):
    """
    Render the homepage of the Golden Sound Bagel Shop.
    """
    return render(request, 'menu/index.html')