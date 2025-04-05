from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect


# Define the Django view to handle scraping and showing scraped links
def scrape(request):

    # Check if the request method is POST (i.e., form submission)
    if request.method == "POST":
        
        # Get the URL from the POST data and strip extra spaces
        site = request.POST.get('site', '').strip()
        
        # If no URL is provided, show an error and redirect back
        if not site:
            messages.error(request, "❌ Please enter a valid URL.")
            return HttpResponseRedirect('/')
        
        try:
            # Send a GET request to the provided site
            page = requests.get(site)

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(page.text, 'html.parser')
            print(soup.prettify())

            # Loop through all anchor tags on the page
            for link in soup.find_all('a'):

                # Get the href (link address)
                link_address = link.get('href')
                print(link_address,'\n')

                # Get the visible text of the link and strip it
                link_text = link.text.strip()
                print(link_text)

                # Save the link into the database
                Link.objects.create(address=link_address, name=link_text)
                data_list = Link.objects.all().order_by('-id')

                # Paginate the results, 10 items per page
                paginator = Paginator(data_list, 10)

                # Get the current page number from the query parameters
                page_number = request.GET.get('page')

                # Get the relevant page of data
                data = paginator.get_page(page_number)

        # Handle any exceptions during the request
        except requests.RequestException as e:
            # Log the error in the console
            print(f"Error fetching site: {e}")
            
            # Redirect back to home page
            return HttpResponseRedirect('/')

        # After processing, redirect to home page
        return HttpResponseRedirect('/')

    # If request method is GET (i.e., viewing page, not submitting)
    else:
        # Get all Link objects ordered by most recent first
        data_list = Link.objects.all().order_by('-id')

        # Paginate the results, 10 items per page
        paginator = Paginator(data_list, 10)

        # Get the current page number from the query parameters
        page_number = request.GET.get('page')

        # Get the relevant page of data
        data = paginator.get_page(page_number)

        # Render the HTML template with the paginated data
    return render(request, 'scrapper/index.html', {'data': data})



def clear(request):
    Link.objects.all().delete()
    return HttpResponseRedirect('/')  
