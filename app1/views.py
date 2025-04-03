from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Pro.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
# from django.contrib.auth.models import AbstractUser
from . models import Admin, Admin_Deleted_Seller_Account, Buyers, Comments, Products, Admin_Deleted_Products, Razorpay_Transaction, Traction_History, Seller
import razorpay
from django.conf import settings
import time
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError, transaction
# from django.contrib.auth.decorators import login_required

# Create your views here.

def main_home_page_function(request):
    if request.method == 'POST':
        nam=request.POST['name']
        fb=request.POST['feed']
        data1=Comments.objects.create(name=nam, body=fb)
        data1.save()
        return redirect(main_home_page_function)
    else:    
        pro=Products.objects.all()
        return render(request, "main_home_page_function.html", {'value': pro})
    
def all_comments_function(request):
    data1=Comments.objects.all()
    return render(request, "all_comments.html", {'value': data1})

def search_function(request):
    # Determine if they fill the form
    if request.method == 'POST':
        searched=request.POST['searched']
        # Lets query the database model
        searched = Products.objects.filter(title__icontains=searched)
        # Test for null
        if not searched:
            messages.warning(request, "This product doesnot exist...")
            return render(request, "search.html", {})
        else:
            time.sleep(2)
            return render(request, "search.html", {'searched': searched})
    else:
        return render(request, "search.html", {})

def goto_main_home_page_function(request):
    return redirect(main_home_page_function)

def back_to_homepage_function(request):
    return redirect(main_home_page_function)

def seller_homepage_return_function(request):
    return redirect(seller_home_function)

def seller_homepage_return_1_function(request):
    return redirect(seller_home_function)

def seller_profile_redirect_function(request):
    return redirect(seller_home_function)


def about_us_readmore_function(request):
    return render(request, "about_us_readmore.html")

def about_us_readmore1_function(request):
    return render(request, "about_us_readmore1.html")

def main_login_function(request):
    if request.method=='POST':
        un=request.POST['username']
        pwd=request.POST['password']
        x=authenticate(request, username=un, password=pwd)
        
        # Admin login session
        # ------------- #
        if x is not None and x.is_superuser == 1:
            login(request, x)
            request.session['admin_id'] = x.id
            time.sleep(3)
            return redirect(admin_home_function)
        
        # Registered Seller session
        # ------------------------------ # 

        elif x is not None and x.usertype == 'Seller':
            login(request, x)
            request.session['User_id'] = x.id
            time.sleep(3)
            return redirect(seller_home_function)
            # return HttpResponse("User Login Page.....")

        # Registered Buyers session
        # -------------------------
        elif x is not None and x.usertype == 'Buyer':
            login(request, x)
            request.session['Buyer_id'] = x.id
            time.sleep(3)
            return redirect(buyer_home_function)
            # return HttpResponse("Buyer Home Page.....")
        else:
            messages.warning(request, "Invalid username or password, please try again......")
            return render(request, "main_login.html")
    else:
        return render(request, "main_login.html")
    
# Seller Registration Activities
# ------------------------------

def seller_registration_function(request):
    try:
        if request.method == 'POST':
            na=request.POST['uname']
            sp=request.FILES.get('spic')
            if not sp:
                sp = 'blank-profile-picture-973460_1280.webp'
            ag=request.POST['uage']
            gn=request.POST['ugender']
            ad=request.POST['uaddress']
            em=request.POST['uemail']
            ph=request.POST['uphoneno']
            un=request.POST['uusername']
            pwd=request.POST['upassword']

            adm=Admin.objects.create_user(username=un, email=em, password=pwd, usertype="Seller")
            ur=Seller.objects.create(fk1=adm, name=na, spic=sp, age=ag, gender=gn, Address=ad,
                                            email=em, number=ph, 
                                            username=un, password=pwd)
            ur.save()
            time.sleep(5)
            return redirect(main_login_function)
        else:
            return render(request, "seller_registration.html")
    except:
        messages.warning(request, "Phone number, email or Password already exist, Please try with diferent details...")
        return render(request, "seller_registration.html")
    
def seller_home_function(request):
    n1=request.session['User_id']
    data=Admin.objects.get(id=n1)
    data1=Seller.objects.get(fk1=data)
    return render(request, "seller_home.html", {'value':data1})

def sell_product_function(request):
    if request.method == 'POST':
        img1=request.FILES['imag1']
        img2=request.FILES['imag2']
        img3=request.FILES['imag3']
        img4=request.FILES['imag4']
        img5=request.FILES['imag5']
        tit=request.POST['title']
        dscr=request.POST['description']
        pri=request.POST['prize']
        n1=request.session['User_id']
        data=Seller.objects.get(fk1=n1)
        # print(data.name)

        card=Products.objects.create(image1=img1, image2=img2, image3=img3, image4=img4, image5=img5, 
                                     title=tit, desc=dscr, prize=pri, fk2=data)
        # print(card)

        card.save()
        time.sleep(2)
        return redirect(seller_home_function)

    else:

        return render(request, "sell_product.html")
    
# Seller Personal Data
# ---------------------
def seller_personal_data_function(request, a):
    # print(a)
    sel=Seller.objects.get(id=a)
    return render(request, "seller_personal_data.html", {'value':sel})



def seller_personal_data_update_function(request, b):
    try:
        if request.method == 'POST':
            spp = request.FILES.get('spic')
            na = request.POST['name']
            ag = request.POST['age']
            gn = request.POST['gender']
            ad = request.POST['address']
            em = request.POST['email']
            nu = request.POST['number']
            un = request.POST['username']
            pwd = request.POST['password']

            seller = Seller.objects.get(id=b)
            admin = seller.fk1

            # Hash the password before saving
            hashed_password = make_password(pwd)

            # Use transaction.atomic to ensure data integrity
            with transaction.atomic():
                # Update Admin table
                admin.password = hashed_password
                admin.username = un
                admin.email = em
                admin.usertype = "Seller"
                admin.save()

                # Update Seller table
                if spp:
                    # print(f"Uploading image1: {spp.name}")
                    # print(seller.spic)
                    seller.spic = spp

                seller.name = na
                seller.age = ag
                seller.gender = gn
                seller.Address = ad
                seller.email = em
                seller.number = nu
                seller.username = un
                seller.password = pwd
                seller.save()

            return redirect(seller_home_function)  # Ensure 'seller_home_function' is a valid URL or view name
        else:
            return redirect(seller_home_function)

    except KeyError:
        return HttpResponse("Something went wrong, please try again later....")
    except IntegrityError:
        return HttpResponse("The username or email already exists. Please try with different details.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")  

def seller_product_function(request, c):
    data=Seller.objects.get(id=c)
    data2=Products.objects.filter(fk2=data.id)
    return render(request, "seller_products_view_individual.html", {'value': data2})


def seller_delete_products_function(request, d):
    data1=Products.objects.get(id=d)
    data1.delete()
    return redirect(seller_home_function)

def seller_view_all_images_function(request, e):
    data1=Products.objects.get(id=e)
    return render(request, "seller_view_all_images.html", {'value': data1})

def seller_edit_image_details(request, f):
    if request.method == 'POST':
        # Get the uploaded images and print them to check
        img1 = request.FILES.get('image1', None)
        img2 = request.FILES.get('image2', None)
        img3 = request.FILES.get('image3', None)
        img4 = request.FILES.get('image4', None)
        img5 = request.FILES.get('image5', None)

        tit = request.POST['tit']
        desc = request.POST['desc']
        prz = request.POST['amnt']

        print(f"image1: {img1}, image2: {img2}, image3: {img3}, image4: {img4}, image5: {img5}")
        print(f"Title: {tit}, Description: {desc}")

        # Get the product object by ID
        data1 = Products.objects.get(id=f)

        # Check if files are present and print file names for debugging
        if img1:
            print(f"Uploading image1: {img1.name}")
            data1.image1 = img1
        if img2:
            print(f"Uploading image2: {img2.name}")
            data1.image2 = img2
        if img3:
            print(f"Uploading image3: {img3.name}")
            data1.image3 = img3
        if img4:
            print(f"Uploading image4: {img4.name}")
            data1.image4 = img4
        if img5:
            print(f"Uploading image5: {img5.name}")
            data1.image5 = img5

        # Update Product Details
        data1.title = tit
        data1.desc = desc
        data1.prize = prz

        # Save the product with the new images and details
        data1.save()

        # Redirect after saving
        return redirect(seller_home_function)

def seller_transactions_function(request):
    n1=request.session['User_id']
    data1=Seller.objects.get(fk1=n1)
    data2=Traction_History.objects.filter(fkseller=data1)
    # print(data2) #op:  Query set
    return render(request, "seller_transactions.html", {'value':data2})

def seller_view_transaction_history_individual_function(request, q):
    # print(q)
    data1=Traction_History.objects.get(id=q)
    return render(request, "seller_view_transaction_history_individual.html", {'value': data1})

def seller_transaction_go_back_button_function(request):
    return redirect(seller_transactions_function)

def about_us_deadmore_guideline_function(request):
    return render(request, "about_us_deadmore_guideline.html")


# Admin Activities
def admin_home_function(request):
    n=request.session['admin_id']
    data=Admin.objects.get(id=n)
    return render(request, "admin_home.html", {'value': data})

def admin_view_all_products_function(request):
    data1=Products.objects.all()
    return render(request, "admin_view_all_products.html", {'value': data1})

def admin_delete_product_function(request, g):
    data1=Products.objects.get(id=g)
    datay=Seller.objects.get(id=data1.fk2.id)
    img1=data1.image1
    img2=data1.image2
    img3=data1.image3
    img4=data1.image4
    img5=data1.image5
    tit=data1.title
    desc=data1.desc
    prize=data1.prize

    data2=Admin_Deleted_Products.objects.create(image1=img1, image2=img2, image3=img3, image4=img4, image5=img5, title=tit, desc=desc, prize=prize, fk3=datay)
    data2.save()

    data3=Products.objects.get(id=g)
    data3.delete()
    return redirect(admin_view_all_products_function)

def admin_view_all_images_function(request, h):
    data1=Products.objects.get(id=h)
    return render(request, "admin_view_all_images.html", {'value': data1})

def admin_view_all_seller_personal_details_function(request):
    data1=Seller.objects.all()
    return render(request, "admin_view_all_seller_personal_details.html", {'value':data1})


def admin_rejected_products_function(request):
    data1=Admin_Deleted_Products.objects.all()
    return render(request, "Admin_Deleted_Products.html", {'value': data1})

def admin_view_rejected_seller_details_function(request, i):
    data1=Admin_Deleted_Products.objects.get(id=i)
    print(data1)
    # datax=Admin_Deleted_Products.objects.filter(fk3=i)
    # print(datax)
    # print(datax)
    return render(request, "admin_view_rejected_seller_details.html", {'value': data1})

def admin_delete_account_of_seller_function(request):
    data1=Seller.objects.all()
    return render(request, "admin_delete_account_of_seller.html", {'value':data1})

def admin_delete_seller_account_function(request, j):
    data1=Seller.objects.get(id=j)
    nm=data1.name
    ag=data1.age
    gn=data1.gender
    ad=data1.Address
    em=data1.email
    num=data1.number
    un=data1.username
    pw=data1.password

    data2=Admin_Deleted_Seller_Account.objects.create(name=nm, age=ag, gender=gn, Address=ad, email=em, number=num, 
                                                      username=un, password=pw)
    data2.save()
    data3=Seller.objects.get(id=j)
    data3.delete()
    data4=Admin.objects.get(id=data3.fk1.id)
    # print(data4.id)
    data4.delete()
    return redirect(admin_delete_account_of_seller_function)

def admin_view_admin_deleted_seller_accounts_function(request):
    data1=Admin_Deleted_Seller_Account.objects.all()
    return render(request, "admin_view_admin_deleted_seller_accounts.html", {'value':data1})

def control_comments_function(request):
    data1=Comments.objects.all()
    return render(request, "admin_control_comments.html", {'value': data1})

def admin_delete_comment_function(request, o):
    # print(o)
    data1=Comments.objects.get(id=o)
    data1.delete()
    return redirect(control_comments_function)

def admin_view_all_transaction_function(request):
    data1=Traction_History.objects.all()
    return render(request, "admin_view_all_transaction.html", {'value': data1})

def admin_view_all_transaction_details_function(request, r):
    # print(r)
    data1=Traction_History.objects.get(id=r)
    # print(data1.odr_id)
    return render(request, "admin_view_all_transaction_details_individual.html", {'value': data1})

def admin_view_buyers_detail_function(request):
    data1=Buyers.objects.all()
    return render(request, "admin_view_buyers_detail.html", {'value':data1})

def admin_view_buyer_products_function(request, r):
    # print(r)
    data2=Buyers.objects.get(id=r)
    
    # print(data2)
    data1=Traction_History.objects.filter(fkbuyer=data2)
    return render(request, "admin_view_buyer_products.html", {'value':data1})

def admin_del_buyer_account_function(request, s):
    data1=Buyers.objects.get(id=s)
    # print(data1.name)
    data1.delete()
    return redirect(admin_view_buyers_detail_function)

# Stranger at homepage (clicked Buy button)
# -----------------------------------------

def login_for_buy_product_function(request, k):
    data1=Products.objects.get(id=k)
    return render(request, "login_for_buy_product.html", {'value':data1})

def redirect_to_login_page_function(request,m):
    time.sleep(2)
    return redirect(main_login_function)

def redirect_to_buyer_registration_function(request):
    return redirect(buyer_registration_function)

# Buyer Registration
# ------------------

def buyer_registration_function(request):
    try:
        if request.method=='POST':
            nam=request.POST['name']
            bp=request.FILES.get('bpic')
            if not bp:
                bp = 'blank-profile-picture-973460_1280.webp'
            ag=request.POST['age']
            gen=request.POST['gender']
            add=request.POST['address']
            ema=request.POST['email']
            phn=request.POST['number']
            un=request.POST['username']
            pwd=request.POST['password']

            data1=Admin.objects.create_user(email=ema, username=un, 
                                            password=pwd, usertype="Buyer")
            
            data2=Buyers.objects.create(fk4=data1, name=nam, bpic=bp, age=ag, gender=gen, Address=add,
                                            email=ema, number=phn, username=un, password=pwd)
            data2.save()
            time.sleep(5)
            return redirect(main_login_function)
        else:
            return render(request, "buyer_registration.html")
    except:
        messages.warning(request, "Phone number, Email or Password already Exists, Please try again with different details....")
        return render(request, "buyer_registration.html")

# Buyer Login
# -----------
def buyer_home_function(request):
    n1=request.session['Buyer_id']
    data=Admin.objects.get(id=n1)        
    data1=Products.objects.all()
    data2=Buyers.objects.get(fk4=data)
    return render(request, "buyer_home.html", {'value':data, 'value1':data1, 'value2':data2})

def buyer_search_function(request):
    # Determine if they fill the form
    if request.method == 'POST':
        searched=request.POST['searched']
        # Lets query the database model
        searched = Products.objects.filter(title__icontains=searched)
        # Test for null
        if not searched:
            messages.warning(request, "This product doesnot exist...")
            return render(request, "buyer_search.html", {})
        else:
            time.sleep(2)
            return render(request, "buyer_search.html", {'searched': searched})
    else:
        return render(request, "buyer_search.html", {})
    
def buyer_return_homepage_function(request):
    return redirect(buyer_home_function)


def buyer_personal_details_function(request, l):
    try:
        if request.method == 'POST':
            bp=request.FILES.get('bp')
            nam=request.POST['name']
            ag=request.POST['age']
            gen=request.POST['gender']
            add=request.POST['address']
            ema=request.POST['email']
            pho=request.POST['number']
            un=request.POST['username']
            pwd=request.POST['password']

            data2=Buyers.objects.get(id=l)
            data3=data2.fk4           # assuming data3 as admin

            with transaction.atomic():
                # Admin Update
                # ------------
                data3.password = make_password(pwd)
                data3.username = un
                data3.email = ema
                data3.usertype = "Buyer"
                data3.save()

            # Buyer update
            # -------------
                if bp:
                    # print(f"Uploading image1: {bp.name}")
                    # print(data2.bpic)
                    data2.bpic=bp 

                                     
                data2.name = nam
                data2.age = ag
                data2.gender = gen
                data2.Address = add
                data2.email = ema
                data2.number = pho
                data2.username = un
                data2.password = pwd
                data2.save()

            return redirect(buyer_home_function)  
            
        else:
            data1=Buyers.objects.get(id=l)
            return render(request, "buyer_personal_details.html", {'value':data1})
    except:
        return HttpResponse("The username or email already exists. Please try with different details....")


from decimal import Decimal
def buyer_home_buy_button_function(request, n):
    data1=Products.objects.get(id=n)
    data3=Products.objects.get(id=n)
    data4=data1.prize
    order_amount = Decimal(data4)
    order_amount_in_paise =float(order_amount * 100)


    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
    payment = client.order.create({'amount': order_amount_in_paise, 'currency': 'INR', 'payment_capture': 1})
    payment_order_id=payment['id']
    payment_order_amount=payment['amount']


    context = {'amount':payment_order_amount, 'payment':payment, 'value':data1}

    data5=Razorpay_Transaction.objects.create(fk5=data3, razor_pay_order_id=payment_order_id)
    data5.save()
    return render(request, "buyer_home_buy_button.html", context)
 
def success(request):
    razorpay_payment_id = request.GET.get('razorpay_payment_id')
    razorpay_order_id = request.GET.get('razorpay_order_id')
    
    # Initialize Razorpay client
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
    
    # Verify the payment
    try:
        payment = client.payment.fetch(razorpay_payment_id)
        if payment['status'] == 'captured':
            # If the payment is successful, mark the transaction as paid
            transaction = Razorpay_Transaction.objects.get(razor_pay_order_id=razorpay_order_id)
            transaction.is_paid = True
            transaction.save()

            n1=request.session['Buyer_id']
            data=Admin.objects.get(id=n1)
            data1=Buyers.objects.get(fk4=data)

            product = transaction.fk5  # Get the product related to this transaction
            seller = product.fk2

            th=Traction_History.objects.create(
                                            #  Product details
                                            #  ---------------  
                                               image1=product.image1, image2=product.image2, image3=product.image3, image4=product.image4, image5=product.image5,
                                               title=product.title, desc=product.desc, prize=product.prize, 
                                            #  Seller details
                                            #  --------------
                                               seller_name=seller.name, seller_age=seller.age, seller_gender=seller.gender, seller_Address=seller.Address, 
                                               seller_email=seller.email, seller_number=seller.number,
                                            #  Buyer details
                                            #  -------------
                                               buyer_name=data1.name, buyer_age=data1.age, buyer_gender=data1.gender, buyer_Address=data1.Address, 
                                               buyer_email=data1.email, buyer_number=data1.number,
                                            #  order id
                                            #  --------
                                               odr_id=transaction.razor_pay_order_id,
                                            #  Foreign Key
                                            #  -----------
                                               fkbuyer=data1, fkseller=seller)
            th.save()

            del_pro=Products.objects.get(id=product.id)
            del_pro.delete()

            return render(request, "transaction_history.html", {'value':th})
        else:
            return HttpResponse("Payment failed or pending!")
    except razorpay.errors.SignatureVerificationError:
        return HttpResponse("Payment Signature Verification Failed.")
    except Razorpay_Transaction.DoesNotExist:
        return redirect(buyer_home_function)
    
def Buyer_transactions_function(request):
    n1=request.session['Buyer_id']
    data1=Buyers.objects.get(fk4=n1)
    data2=Traction_History.objects.filter(fkbuyer=data1)
    return render(request, "Buyer_transactions.html", {'value':data2})

def buyer_transaction_individual_item_full_details_function(request, p):
    data1=Traction_History.objects.get(id=p)
    # print(data1.desc)
    return render(request, "buyer_transaction_individual_item_full_details.html", {'value':data1})

def buyer_goback_button_to_all_transaction_function(request):
    print(request)
    return redirect(Buyer_transactions_function)

# Logouts (Buyer, Seller, Admin)
# ------------------------------
def buyer_logout_function(request):
    logout(request)
    time.sleep(2)
    return redirect(main_home_page_function)

def seller_logout_function(request):
    logout(request)
    time.sleep(2)
    return redirect(main_home_page_function)

def admin_logout_function(request):
    logout(request)
    time.sleep(2)
    return redirect(main_home_page_function)