from django.urls import path
from . import views
from gym_management_app.settings import DEBUG, STATIC_URL, MEDIA_URL, MEDIA_ROOT

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import request_leave

from django.conf import settings
from django.contrib.auth import views as auth_views


from .views import add_product


urlpatterns = [
    path('', views.index, name = 'index'),
   	# path('admin/', views.adminlogin, name="adminlogin"),
    # path('adminpanel/',views.adminpanel,name="adminpanel"),
    # path('login/', views.login,name='login'),
    path('member_login/', views.member_login, name='member_login'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('request_leave/', views.request_leave, name='request_leave'),
    

    path('bmi-calculator/', views.bmi_calculator, name='bmi_calculator'),
    path('services/', views.services, name='services'),
    path('classes/', views.classes, name='classes'),


    path('contacts/', views.contacts, name='contacts'),

    path('class-timetable/', views.class_timetable, name='class_timetable'),

    path('booking/', views.booking_view, name='booking'),
    path('book/', views.book, name='book'),


    

    path('appointment/', views.appointment_view, name='appointment'),
    path('shop/', views.shop, name='shop'),
    


    path('registration/', views.registration, name="registration"),
    path('trainer_login/', views.trainer_login, name="trainer_login"),

    path('consultant_login/', views.consultant_login, name="consultant_login"),
    path('consultant_dashboard/', views.consultant_dashboard, name='consultant_dashboard'),
    path('send-notification/', views.send_notification, name='send_notification'),
    # Add other URLs as needed

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout, name="logout"),
    path('home/', views.home, name="home"),
    path('view_bill/', views.view_bill, name="view_bill"),
 	path('view_diet/', views.view_diet, name = 'view_diet'),
    path('view_schedule/', views.view_schedule, name = 'view_schedule'),
    path('view_store/', views.view_store, name = 'view_store'),
    
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_login', views.admin_login, name='admin_login'),
    

    path('trainer_list/', views.trainer_list, name='trainer_list'),
    path('trainer_detail/<int:trainer_id>/', views.trainer_detail, name='trainer_detail'),
    path('trainer_add/', views.trainer_add, name='trainer_add'),
    path('trainer_edit/<int:trainer_id>/edit/', views.trainer_edit, name='trainer_edit'),
    path('trainer_delete/<int:trainer_id>/delete/', views.trainer_delete, name='trainer_delete'),

    path('consultant_list/', views.consultant_list, name='consultant_list'),
    path('consultant_detail/<int:consultant_id>/', views.consultant_detail, name='consultant_detail'),
    path('consultant_add/', views.consultant_add, name='consultant_add'),
    path('consultant_edit/<int:consultant_id>/edit/', views.consultant_edit, name='consultant_edit'),
    path('consultant_delete/<int:consultant_id>/delete/', views.consultant_delete, name='consultant_delete'),
    
    path('user_list/', views.user_list, name='user_list'),
    path('member_detail/<int:pk>/', views.member_detail, name='member_detail'),
    path('add_member/', views.add_member, name='add_member'),
    path('edit_member/<int:pk>/edit/', views.edit_member, name='edit_member'),
    path('delete_member/<int:pk>/delete/', views.delete_member, name='delete_member'),

    path('bill_list/', views.bill_list, name='bill_list'),
    # path('bill_detail/<int:bill_id>/', views.bill_detail, name='bill_detail'),
    path('bill_add/add/', views.bill_add, name='bill_add'),
    # path('bill_edit/<int:pk>/edit/', views.bill_edit, name='bill_edit'),
    # path('bill_delete/<int:pk>/delete/', views.bill_delete, name='bill_delete'),
    path('bill_detail/detail/<int:pk>/', views.bill_detail, name='bill_detail'),
    path('bill_edit/<int:pk>/edit/', views.bill_edit, name='bill_edit'),
    path('bill_delete/<int:pk>/delete/', views.bill_delete, name='bill_delete'),
    # Other URLs...

    path('store_list/', views.store_list, name='store_list'),
    path('store_detail/<int:pk>/', views.store_detail, name='store_detail'),
    path('store_add/add/', views.store_add, name='store_add'),

    path('schedule_list/', views.schedule_list, name='schedule_list'),
    path('schedule_detail/<int:pk>/', views.schedule_detail, name='schedule_detail'),
    path('schedule_add/', views.schedule_add, name='schedule_add'),

    path('diet_list/', views.diet_list, name='diet_list'),
    path('diet_detail/<int:pk>/', views.diet_detail, name='diet_detail'),
    path('diet_add/', views.diet_add, name='diet_add'),


    # URL pattern for the shop view
    path('shop/', views.shop, name='shop'),

    # URL pattern for the product details view
    path('product/<int:id>/', views.product_details, name='product_details'),

    # URL pattern for the get product details view
    path('product_details/', views.get_product_details, name='get_product_details'),

    # URL pattern for the products by subcategory view
    # Add the correct URL pattern for products by subcategory view
    path('products-by-subcategory/<str:subcategory>/', views.products_by_subcategory, name='products_by_subcategory'),

    path('add_product/', views.add_product, name='add_product'),

    
   
       ] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)