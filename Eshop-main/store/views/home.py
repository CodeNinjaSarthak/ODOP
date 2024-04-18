from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View
import pyrebase
from django.urls import reverse

#firebase
config={
	"apiKey": "AIzaSyB5a7Mc42hl0_-fvCAcMiVXQ4As0dlbBJ8",
	"authDomain": "project-216c2.firebaseapp.com",
	"databaseURL": "https://project-216c2-default-rtdb.firebaseio.com",
	"projectId": "project-216c2",
	"storageBucket": "project-216c2.appspot.com",
	"messagingSenderId": "908044867759",
	"appId": "1:908044867759:web:c638e62ec8bbd498cf1c5a",
	"measurementId": "G-LJ94XCQXC4"
}

firebase=pyrebase.initialize_app(config)
database=firebase.database()
authe = firebase.auth()
# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)





# view for vendor registration
# def vendor_registration(request):
#     # return render(request, 'vendor_registration.html')
#     if request.method == 'POST':
#         username = request.POST.get('Username')
#         email = request.POST.get('Email')
#         addhar = request.POST.get('Addhar')
#         phone = request.POST.get('Phone')
#         passs = request.POST.get('Password')
#         try:
            
            
#             user_data = {
#                 'Username': username,
#                 'Email': email,
#                 'Addhar': addhar,
#                 'Phone': phone,
#                 'Password' : passs, 
                
#             }

#             # database.push(user_data)
#             database.push(user_data)
#             return render(request, "vendor_login.html")
#         except Exception as e:
#             # Log error message
#             print(f"Error saving data to Firebase: {str(e)}")
#             return render(request, "vendor_login.html")
#     else:
#         # If request method is not POST, render the registration form
#         return render(request, "vendor_registration.html")
# # view for vendor Login
# def vendor_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('Email')
#         password = request.POST.get('Password')
#         try:
#             user = authe.sign_in_with_email_and_password(email, password)
#             # Redirect to another page after successful login
#             return redirect('index.html')  
#         except Exception as e:
#             message = "Invalid email or password. Please check your credentials."
#         return render(request, 'vendor_login.html', {"message": message})
#     return render(request, 'vendor_login.html')
def vendor_registration(request):
   
    if request.method == 'POST':
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        addhar = request.POST.get('Addhar')
        phone = request.POST.get('Phone')
        passs = request.POST.get('Password')
        try:
            user=authe.create_user_with_email_and_password(email,passs)
            uid = user['localId']
            idtoken = request.session['uid']
            return render(request, 'vendor_login.html')
        except:
            return render(request, "vendor_registration.html")
    return render(request,"vendor_registration.html")
    
def vendor_login(request):
    # email=request.POST.get('Email')
    # pasw=request.POST.get('Password')
    # try:
    #     # if there is no error then signin the user with given email and password
    #     user=authe.sign_in_with_email_and_password(email,pasw)
    # except:
    #     message="Invalid Credentials!!Please ChecK your Data"
    #     return render(request,"Login.html",{"message":message})
    # session_id=user['idToken']
    # request.session['uid']=str(session_id)
    # return render(request,"index.html",{"email":email})
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = authe.sign_in_with_email_and_password(email, password)
                # Redirect to another page after successful login
                return redirect('hello')  
            except Exception as e:
                message = "Invalid email or password. Please check your credentials."
            return render(request, 'vendor_login.html', {"message": message})
        return render(request, 'vendor_login.html')

def hello_view(request):
    return render(request, 'hello.html')

