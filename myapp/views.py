from django.shortcuts import render
from .models import data


def index(request):
    return render(request, "index.html")
def collection(request):
    return render(request, "collection.html")
def theartofelorian(request):
    return render(request, "theartofelorian.html")
def contact(request):
    return render(request, "contact.html")
def address(request):
    if request.method == "POST":
        Fullname = request.POST['fullname']
        Mobile = request.POST['mobile']
        Email = request.POST['email']
        Address1 = request.POST['address1']
        Address2 = request.POST['address2']
        Landmark = request.POST['landmark']
        City = request.POST['city']
        State = request.POST['state']
        Pincode = request.POST['pincode']

        obj = data()
        obj.fullname = Fullname
        obj.mobile = Mobile
        obj.email = Email
        obj.address1 = Address1
        obj.address2 = Address2
        obj.landmark = Landmark
        obj.city = City
        obj.state = State
        obj.pincode = Pincode
        obj.save()
        

        return render(request, "payment.html")
    return render(request, "address.html")

def payment(request):
    return render(request, "payment.html")
def login(request):
    return render(request, "login.html")
def success(request):
    return render(request, "success.html")