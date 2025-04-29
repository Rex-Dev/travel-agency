from django.contrib import messages
from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from .models import Package, User, Booking
from django.views.decorators.http import require_http_methods
# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    if request.method=='POST':
        user_name=request.POST.get('user_name')
        phno=request.POST.get('phno')
        pswd=request.POST.get('pswd')
        user=User(user_name=user_name,phno=phno,pswd=pswd)
        user.save()
        return redirect('login')
    return render(request,"register.html")

from django.contrib.auth import authenticate, login



def login(request):
    if request.method == 'POST':
        phno = request.POST.get('phno')
        pswd = request.POST.get('pswd')
        try:
            user = User.objects.get(phno=phno)
            if user.pswd == pswd:  # Password check (not recommended, see below)
                request.session['phno'] = user.phno
                return redirect('packages')
            else:
                return render(request, "login.html", {'error': 'Invalid credentials'})
        except User.DoesNotExist:
            return redirect('register')
    return render(request, "login.html")

def packages(request):
    packages = Package.objects.filter(is_active=True)
    for package in packages:
        package.split_destinations = package.package_destinations.split(",")
    return render(request, "packages.html", {"packages": packages})



from django.shortcuts import redirect
@require_http_methods(["GET", "POST"])
def booking_page(request, package_name):
    if not package_name:  # ✅ Ensure package_name exists
        messages.error(request, "Invalid package selection.")
        return redirect('packages')

    package = get_object_or_404(Package, package_name=package_name)
    phno = request.session.get('phno')
    amount = package.package_price

    if Booking.objects.filter(phno=phno, package_name=package_name, status="Requested").exists():
        messages.error(request, "You have already booked this package.")
        return redirect('packages')

    if request.method == "POST":
        persons = request.POST.get('persons')
        date = request.POST.get('booking_date')
        payment_method = request.POST.get('pm')

        if not persons or not date or not payment_method:
            return render(request, "booking_page.html", {"package": package, "package_name": package_name})

        amt = amount * int(persons)  # ✅ Ensure persons is an integer
        booking = Booking(
            amt=amt, status="Requested", payment_address="example_address",
            package_name=package.package_name, persons=persons,
            date=date, payment_method=payment_method, phno=phno, user_name=phno
        )
        booking.save()

        messages.success(request, f"Booking successful! Amount paid: {amt}")
        return redirect('booking_page', package_name=package_name)

    return render(request, "booking_page.html", {"package": package, "package_name": package_name})


