from django.shortcuts import get_object_or_404, redirect, render 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import LeaveRequestForm
from .models import LeaveRequest

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import UserProfile  # Import UserProfile if you have it

# from django.contrib.auth import logout as auth_logout
# from django.http import HttpResponseRedirect
# from django.urls import reverse


from django.shortcuts import render
from django.http import HttpResponseRedirect
# from .models import Booking

from .models import Member
from .forms import MemberForm
# from .forms import MemberForm
from .models import Bill
from .forms import BillForm

from .models import Trainer
from .forms import TrainerForm

from .models import Consultant
from .forms import ConsultantForm

from .models import Store
from .forms import StoreForm

from .models import Schedule
from .forms import ScheduleForm  # Assuming you have a form class for Schedule

from .models import Diet
from .forms import DietForm  # Assuming you have created a DietForm

from .forms import LeaveRequestForm
from .models import LeaveRequest

from .models import Product1

# from .forms import 
# from .filters import 
from datetime import date,datetime
import os
from django.contrib import auth
from .models import *




def home(request):
    return render(request, 'gym/home.html')

def index(request):
    return render(request, 'gym/index.html')
# def adminlogin(request):
#     return redirect('admin')

# def adminpanel(request):
#     return render(request,'adminpanel.html')

def bmi_calculator(request):
    return render(request, 'bmi_calculator.html')  # Assuming your BMI calculator template is named bmi_calculator.html

def services(request):
    return render(request, 'services.html') 

def classes(request):
    return render(request, 'classes.html')

def contacts(request):
    return render(request, 'contacts.html')

def class_timetable(request):
    return render(request, 'class_timetable.html')

def edit_profile(request):
    # Your logic for handling profile editing goes here
    return render(request, 'edit_profile.html')

def member_login(request):
    if request.method == 'POST':
        try:
            user=Member.objects.get(Email = request.POST['Email'],Password= request.POST['Password'])
            return redirect('home')
            
        except Member.DoesNotExist:
            return render (request,'gym/member_login.html', {'error':'Username or password is incorrect!'})
   
    else:
    
        return render(request, 'gym/member_login.html')

def booking_view(request):
    if request.method == 'POST':
        # Process the booking form
        pass
    else:
        # Render the booking form template
        return render(request, 'booking_form.html')
    

    
def book(request):
    if request.method == 'POST':
        # Process form data here
        # Example: Save booking information to the database
        date = request.POST.get('date')
        time = request.POST.get('time')
        doctor = request.POST.get('doctor')
        # Perform necessary actions with the booking data
        # Redirect to a success page or render a confirmation message
    else:
        return render(request, 'booking_form.html')
    
def leave_request_view(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            # Process the form data
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            reason = form.cleaned_data['reason']
           
    else:
        form = LeaveRequestForm()

    return render(request, 'leave_request.html', {'form': form})

def request_leave(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            reason = form.cleaned_data['reason']
            
           
            return render(request, 'success_page.html')  # Or render a success page
    else:
        form = LeaveRequestForm()

    return render(request, 'leave_request.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')

def admin_manage_leave(request):
    if request.method == 'POST':
        leave_request_id = request.POST.get('leave_request_id')
        status = request.POST.get('status')
        leave_request = LeaveRequest.objects.get(pk=leave_request_id)
        leave_request.status = status
        leave_request.save()
        # Add notification logic here
    leave_requests = LeaveRequest.objects.filter(status='Pending')
    return render(request, 'admin_manage_leave.html', {'leave_requests': leave_requests})

def leave_request_notification(request):
    leave_requests = LeaveRequest.objects.filter(user=request.user)
    return render(request, 'leave_request_notification.html', {'leave_requests': leave_requests})



def appointment_view(request):
    if request.method == 'POST':
        # Process the appointment form
        pass
    else:
        # Render the appointment form template
        return render(request, 'appointment_form.html')
    
from django.shortcuts import render

def shop(request):
    # You may need to pass additional context variables here
    return render(request, 'shop.html')

def add_product(request):
    if request.method == 'POST':
        category_name = request.POST.get('category-name')
        category, created = Category1.objects.get_or_create(name=category_name)

        # Retrieve or create the Subcategory2 instance while providing the Category2 instance
        subcategory_name = request.POST.get('subcategory-name')
        subcategory, created = Subcategory1.objects.get_or_create(name=subcategory_name, category=category)

        # Handle the form submission
        product_name = request.POST.get('product-name')
        stock = request.POST.get('stock')  # Retrieve quantity from the form
        description = request.POST.get('description')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        status = request.POST.get('status')
        product_image = request.FILES.get('product-image')

        price = float(price)
        discount = float(discount)

        # Calculate sale_price
        sale_price = price - (price * (discount / 100))

        # Create a new Product2 object and save it to the database
        product = Product1(
            product_name=product_name,
            category=category,
            subcategory=subcategory,
            stock=stock,  # Assign the quantity field
            description=description,
            price=price,
            discount=discount,
            sale_price=sale_price,
            status=status,
            product_image=product_image,
        )
        product.save()

        # Redirect to a success page or any other desired action
        # return redirect('viewproduct')

    return render(request, 'addproduct.html')

def product_details(request, id):
    # Retrieve the product details from the database
    product = get_object_or_404(Product1, id=id)

    # Render the product details template with the product data
    return render(request, 'product_details.html', {'product': product})


def get_product_details(request):
    # Retrieve the product details (you can modify this based on your requirements)
    products = Product1.objects.all()
    product_data = []

    for product in products:
        product_data.append({
            
            'product_name': product.product_name,
            'category': product.category,
            'subcategory': product.subcategory,
            'stock': product.stock,
            'description': product.description,
            'price': product.price,
            'discount': product.discount,
            'sale_price': product.sale_price,
            'status': product.status,
            'product_image': product.product_image.url,
        })

    return render(request, 'product_details.html', {'products': product_data})

from django.shortcuts import get_list_or_404
def products_by_subcategory(request, subcategory):
    # Retrieve a list of Subcategory1 objects based on the provided subcategory name
    subcategories = get_list_or_404(Subcategory1, name=subcategory)

    # Retrieve products based on the list of Subcategory1 objects
    products = Product1.objects.filter(subcategory__in=subcategories)

    return render(request, 'products.html', {'products': products})
    
def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to admin dashboard upon successful login
        else:
            # Authentication failed, show error message
            return render(request, 'admin_login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'admin_login.html')

def user_login(request):
    if request.method == 'POST':
        try:
            user=Member.objects.get(Email = request.POST['Email'],Password= request.POST['Password'])
            return redirect('admin')
            
        except Member.DoesNotExist:
            return render (request,'gym/member_login.html', {'error':'Username or password is incorrect!'})
   
    else:
    
        return render(request, 'gym/member_login.html')
    
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirmPassword', None)
        age = request.POST.get('age', None)
        height = request.POST.get('height', None)
        weight = request.POST.get('weight', None)
        address = request.POST.get('address', None)
        mobile = request.POST.get('mobile', None)

        # Add validation for new fields as needed

        if username and email and password and age and height and weight and address and mobile:
            if User.objects.filter(email=email, username=username).exists():
                messages.success(request, "Email is already registered.")
            elif password != confirm_password:
                messages.success(request, "Passwords don't match. Enter correct password.")
            else:
                user_model = User.objects.create_user(username=username, email=email, password=password)
                user_model.save()

                # # Create UserProfile instance for the user
                # user_profile = UserProfile(user=user_model, age=age, height=height, weight=weight, address=address, mobile=mobile)
                # user_profile.save()

                # Create Member object with user reference
                member = Member.objects.create(
                    user=user_model,
                    age=age,
                    height=height,
                    weight=weight,
                    address=address,
                    mobile=mobile
                )
                member.save()

                return redirect('member_login')

    return render(request, 'gym/registration.html')




def trainer_login(request):
    if request.method == 'POST':
        try:
            user = Trainer.objects.get(Email=request.POST['Email'], Password=request.POST['Password'])
            return redirect('home')
        except Trainer.DoesNotExist:
            return render(request, 'gym/trainer_login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'gym/trainer_login.html')

def consultant_login(request):
    if request.method == 'POST':
        try:
            user = Consultant.objects.get(Email=request.POST['Email'], Password=request.POST['Password'])
            # Redirect to the consultant_dashboard page
            return redirect('consultant_dashboard')
        except Consultant.DoesNotExist:
            return render(request, 'gym/consultant_login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'gym/consultant_login.html')
# views.py
# def consultant_dashboard(request):
#     if request.user.is_authenticated:
#         try:
#             consultant = request.user.consultant
#             # Do something with the consultant object...
#         except Consultant.DoesNotExist:
#             # Handle the case where the user is not associated with a consultant
#             pass
#     else:
#         # Handle the case where the user is not authenticated
#         pass

def consultant_dashboard(request):
    try:
        consultant = request.user.consultant
        # Assuming you have bookings associated with the consultant
        bookings = consultant.booking_set.all()
        return render(request, 'consultant_dashboard.html', {'consultant_name': consultant.user.username, 'bookings': bookings})
    except Consultant.DoesNotExist:
        # Handle the case where the user is not a consultant
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

# @login_required
# def consultant_dashboard(request):
#     consultant = request.user.consultant  # Assuming the consultant is associated with a user
#     bookings = Booking.objects.filter(consultant=consultant)
#     return render(request, 'consultant_dashboard.html', {'consultant_name': consultant.name, 'bookings': bookings})



@login_required
def send_notification(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        # Code to send notification
        # You can use messaging services or email services to send notifications
        messages.success(request, 'Notification sent successfully.')
        return HttpResponseRedirect('/consultant/dashboard/')
    else:
        return HttpResponseRedirect('/consultant/dashboard/')


def view_bill(request):
   
    Email=request.COOKIES['Email']
    getdata = Bill.objects.filter(Customer_id=Email)
    
    #if not getdata and getdata is None:        
    if getdata.exists():
        get_amount=Bill.objects.values_list('Amount', flat=True).get(Customer_id=Email)
        get_payed=Bill.objects.values_list('Payed', flat=True).get(Customer_id=Email)
        Balance=int(get_amount)-int(get_payed)
        return render(request, 'gym/view_bill.html', {'getdata': getdata,'Balance': Balance})
    else :
       return render (request,'gym/view_bill.html', {'error':'there is no Bill'})

def view_diet(request):
    getdata = Diet.objects.all()
    
    if not getdata:
       return render (request,'gym/view_diet.html', {'error':'there is no diet'})
    
    else :
       
        return render(request, 'gym/view_diet.html', {'getdata': getdata})


def view_schedule(request):
    getdata = Schedule.objects.all()
    
    if not getdata:
       return render (request,'gym/view_schedule.html', {'error':'there is no schedule'})
    
    else :
       
        return render(request, 'gym/view_schedule.html', {'getdata': getdata})



def view_store(request):
    getdata = Store.objects.all()
    
    if not getdata:
       return render (request,'gym/view_store.html', {'error':'there is no supplements'})
    
    else :
       
        return render(request, 'gym/view_store.html', {'getdata': getdata})
    


# def logout(request):
#     auth_logout(request)
#     return HttpResponseRedirect(reverse('index'))  # Redirect to the index page

def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index') 

def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))  # Redirect to login page after logout


def admin_dashboard(request):
    return render(request, 'gym/admin_dashboard.html')

def user_list(request):
    users = Member.objects.all()
    return render(request, 'user_list.html', {'users': users})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer_list.html', {'trainers': trainers})

def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    return render(request, 'trainer_detail.html', {'trainer': trainer})

def trainer_add(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
    else:
        form = TrainerForm()
    return render(request, 'gym/trainer_add.html', {'form': form})

def trainer_edit(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_edit.html', {'form': form})

def trainer_delete(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    if request.method == 'POST':
        trainer.delete()
        return redirect('trainer_list')
    return render(request, 'trainer_delete.html', {'trainer': trainer})



def consultant_list(request):
    consultant = Consultant.objects.all()
    return render(request, 'consultant_list.html', {'consultant': consultant})

def consultant_detail(request, consultant_id):
    consultant = get_object_or_404(Consultant, pk=consultant_id)
    return render(request, 'consultant_detail.html', {'consultant': consultant})

def consultant_add(request):
    if request.method == 'POST':
        form = ConsultantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultant_list')  # Redirect to the consultant_list view
    else:
        form = ConsultantForm()
    return render(request, 'consultant_add.html', {'form': form})

def consultant_edit(request, consultant_id):
    consultant = get_object_or_404(Consultant, pk=consultant_id)
    if request.method == 'POST':
        form = ConsultantForm(request.POST, instance=consultant)
        if form.is_valid():
            form.save()
            return redirect('consultant_list')
    else:
        form = ConsultantForm(instance=consultant)
    return render(request, 'consultant_edit.html', {'form': form})


def consultant_delete(request, consultant_id):
    consultant = get_object_or_404(Consultant, pk=consultant_id)
    if request.method == 'POST':
        consultant.delete()
        return redirect('consultant_list')
    return render(request, 'consultant_delete.html', {'consultant': consultant})


def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'member_detail.html', {'member': member})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to the member list page after successfully adding member
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})

def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'edit_member.html', {'form': form})

def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('user_list')
    return render(request, 'delete_member.html', {'member': member})



def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'gym/bill_list.html', {'bills': bills})


# def bill_detail(request, bill_id):
#     bill = get_object_or_404(Bill, pk=bill_id)
#     return render(request, 'bill_detail.html', {'bill': bill})
def bill_detail(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    return render(request, 'gym/bill_detail.html', {'bill': bill})

def bill_add(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'bill_add.html', {'form': form})

def bill_edit(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm(instance=bill)
    return render(request, 'bill_edit.html', {'form': form})

def bill_delete(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('bill_list')
    return render(request, 'bill_delete.html', {'bill': bill})


def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store_list.html', {'stores': stores})

def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'store_detail.html', {'store': store})

def store_add(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store_list')
    else:
        form = StoreForm()
    return render(request, 'store_add.html', {'form': form})

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule_list.html', {'schedules': schedules})

def schedule_detail(request, pk):
    schedule = Schedule.objects.get(pk=pk)
    return render(request, 'schedule_detail.html', {'schedule': schedule})

def schedule_add(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'schedule_add.html', {'form': form})


def diet_list(request):
    diets = Diet.objects.all()
    return render(request, 'diet_list.html', {'diets': diets})

def diet_detail(request, pk):
    diet = Diet.objects.get(pk=pk)
    return render(request, 'diet_detail.html', {'diet': diet})

def diet_add(request):
    if request.method == 'POST':
        form = DietForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the diet list page after successfully adding the diet
            return redirect('diet_list')
    else:
        form = DietForm()
    return render(request, 'diet_add.html', {'form': form})
