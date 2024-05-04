from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from myapp.models import Branch, Voucher
import json
# Create your views here.

def index(request):
    if request.method == "GET":
        branchs = Branch.objects.all()
        voucher = Voucher.objects.all()
        return render(request, 'index.html',{'branchs':branchs,'voucher':voucher})
    if request.method == "POST":
        Voucher.objects.create(
            counter_id = request.POST.get('counter_id'),
            cashier_name = request.POST.get('cashier_name'),
            customer_name = request.POST.get('customer_name'),
            branch_id = request.POST.get('branch'),
            date = request.POST.get('date'),
            total = request.POST.get('total'),
            items = request.POST.get('items')
        )
        return redirect('/voucher/')
    
def detail(request, id):
    branchs = Branch.objects.all()
    voucher = get_object_or_404(Voucher, id=id)
    voucher.date = voucher.date.strftime('%Y-%m-%d')
    items = json.loads(voucher.items) if voucher.items else []
    return render(request, 'detail.html',{'branchs':branchs,'voucher':voucher,'items': items})

def update(request, id):
    voucher = get_object_or_404(Voucher, id=id)

    if request.method == 'POST':
        voucher.counter_id = request.POST.get('counter_id')
        voucher.cashier_name = request.POST.get('cashier_name')
        voucher.customer_name = request.POST.get('customer_name')
        branch_id = request.POST.get('branch')
        voucher.branch = Branch.objects.get(id=branch_id)
        voucher.date = request.POST.get('date')
        voucher.totel = request.POST.get('total')
        items = json.loads(request.POST.get('items'))
        voucher.items = json.dumps(items)
        voucher.save()
        return redirect('/voucher/')
    
def delete(request, id):
    voucher = get_object_or_404(Voucher, id=id)
    voucher.delete()
    return redirect('/voucher/')