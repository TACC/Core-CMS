from django.shortcuts import render

def SearchPageView(request):
    return render(request, 'search_page/search_page.html')
