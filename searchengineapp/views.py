from django.shortcuts import render
from django.shortcuts import render
from django.core.files import File
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
from .models import Docs


def unzipRead(htmlFiles):
    hyperLinksPerHTML = {}
    with ZipFile('cheDoc.zip', 'r') as zip_object:
        for file in htmlFiles:
            with zip_object.open(file) as doc:
                soup = BeautifulSoup(doc, "html.parser")
                # Store hyperlinks, may be useful later in Part 3 or can be appended to the docTable
                hyperLinksPerHTML[file] = [links.get('href') for links in soup.find_all('a', href=True)]
                currentFileText = soup.get_text().lower().split()
                print(currentFileText)
    return HttpResponse()

# ok what the heck
def htmlfiles(request):
  
    doc_list = Docs.objects.all()
    return render(request, 'searchengineapp/search.html', {'doc_list':doc_list})


def index(request):
    return render(request,'searchengineapp/index.html')


def search(request):
    
    if request.method == 'POST':
        search = request.POST['search']


    return render(request,'searchengineapp/search.html', {'search':search})








    # def unzipRead(htmlFiles):
#     archive = ZipFile('cheDoc.zip', 'r')
#     for file in htmlFiles:
#         with archive.open(file) as f1:
#             print(f1.readlines())
    
#     return HttpResponse()

# def unzipRead(htmlFiles):
#     archive = ZipFile('cheDoc.zip', 'r')

# #    # print(archive) prints
#     for item in htmlFiles:
#         with archive.open(item) as file:
#             soup = BeautifulSoup(file, "html.parser")
#             print(file)
#     return HttpResponse()
