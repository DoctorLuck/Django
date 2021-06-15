from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Note
# Create your views here.
def testPaginator(request):
    note_list = Note.objects.all()
    paginator = Paginator(note_list,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'分页.html',{
        'page_obj':page_obj
    })
    # return HttpResponse('测试分页功能')