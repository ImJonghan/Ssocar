from django.shortcuts import render
from .models import Car, Customer
# Create your views here.
# 전체 자동차 리스트
def index(request):
    objs = Car.objects.all() # query set
    context = {
        "cars":objs
    }
    return render(request, template_name="business/index.html", context=context)

# 어떤 고객이 어떤 차를 빌려갔는지 표시하는 detail view
def customer_detail(request, customer_id):
    c = Customer.objects.get(id=customer_id) # 샘알트먼 정보를 뽑기
    context = {
        "customer":c
    } # 뽑은 정보를 context에 담기 -> template으로 보낸다
    return render(request, template_name="business/detail.html", context=context)
