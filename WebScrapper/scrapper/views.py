from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect


def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '').strip()  # ✅ Ensure site URL is properly stripped

        if not site:  # ✅ Prevent empty site submission
            messages.error(request, "❌ Please enter a valid URL.")  # ✅ Show error message           
            return HttpResponseRedirect('/')

        try:
            page = requests.get(site)
            soup = BeautifulSoup(page.text, 'html.parser')

            for link in soup.find_all('a'):
                link_address = link.get('href') or "No URL"  # ✅ Handle missing href
                link_text = link.string or "No Text"  # ✅ Handle missing text
                Link.objects.create(address=link_address, name=link_text)

        except requests.RequestException as e:
            print(f"Error fetching site: {e}")
            return HttpResponseRedirect('/')

        return HttpResponseRedirect('/')

    else:
        data_list = Link.objects.all().order_by('-id')  # ✅ Fetch all links, latest first
        paginator = Paginator(data_list, 10)  # ✅ Show 10 links per page

        page_number = request.GET.get('page')  # ✅ Get page number from URL
        data = paginator.get_page(page_number)  # ✅ Get paginated data

    return render(request, 'scrapper/index.html', {'data': data})



def clear(request):
    Link.objects.all().delete()
    return HttpResponseRedirect('/')  
