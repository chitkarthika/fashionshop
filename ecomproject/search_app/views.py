from django.shortcuts import render
from ecomapp.models import Product
from django.db.models import Q
# Create your views here.
def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        # selecting all products whose name or description matches with query q
        products=Product.objects.all().filter(Q(name__contains=query)| Q(desc__contains=query))
        # printing the matched products name
        for i in products:
            print(i.name)
        print(list(products))
    return render(request,'search.html',{'query':query,'products':products})
