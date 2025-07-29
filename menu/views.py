from django.shortcuts import render
from .models import Bagel # Import the Bagel model to use in views

# Create your views here.
def homepage(request):
    """
    Render the homepage of the Golden Sound Bagel Shop.
    """
    bagels = Bagel.objects.all()  # Fetch all Bagel objects from the database
    context = {
        'bagels': bagels  # Pass the bagels into a dictionary for the template
    }
    return render(request, 'menu/index.html', context)