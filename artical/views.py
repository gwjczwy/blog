from django.shortcuts import render
from .models import Artical
import markdown

def index(request):
    last_artical_list = Artical.objects.order_by('created')
    context={'latest_artical_list':last_artical_list}
    return render(request,'artical/index.html',context)

def artical(request,slug):
    articalObject=Artical.GetArtical(title=slug)
    last_artical_list = Artical.objects.order_by('created')
    if articalObject==False:
        context={
            'title':'页面不存在',
            'body':'您访问的网址有误,请检查拼写'
        }
    else:
        #对markdown进行转义
        articalObject.body = markdown.markdown(articalObject.body,
            extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            ])
        #对文章文本进行分段
        articalObject.body=articalObject.body.split('\r\n')
        context={
            'articalObject':articalObject,
            'latest_artical_list': last_artical_list
        }
    return render(request, 'artical/articals.html', context)

def test(request):
    return render(request, 'artical/test.html')
