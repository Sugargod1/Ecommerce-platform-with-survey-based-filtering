from django.shortcuts import render, redirect
from .models import Product
final_rec_products = []  # Define final_rec_products globally

def survey(request):
    global final_rec_products  # Declare the usage of the global variable
    if request.method == 'POST':
        # Process the survey form data
        # Get the selected choices from the form
        usage_place = request.POST.get('q1')
        operating_system = request.POST.get('q3')
        laptop_size = float(request.POST.get('q5'))

        # Now, based on the survey results, filter the products
        filtered_products = Product.objects.all()
        final_rec_products = []
        for item in filtered_products:
            if operating_system == item.operating_system and laptop_size - 2 <= item.mobileness <= laptop_size + 1 and usage_place == item.office:
                final_rec_products.append(item)  # Append item to final_rec_products
        return redirect('store')  # Redirect to the store URL, not a template
    else:
        return render(request, 'store/survey.html', {})
def store(request):
    global final_rec_products  # Declare the usage of the global variable
    # Your view logic here
    return render(request, 'store/store.html', {'store_list': final_rec_products})
