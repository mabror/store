from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, IncomeForm, ExpenceForm, ProductForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Income, Outgoung


def page(request):
    return render(request, 'page.html', {})


def home(request):
    """ Home page """
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


#CREATE_POST
def post_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                return redirect('page')
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'post_create.html', context)



#history
def current_product(request, product_id):
    if request.method == 'POST':
        print(request.POST['id'])
    product = Income.objects.filter(product_id=product_id).order_by('-added')
    context = {'current_product': product}
    return render(request, 'product.html', context)


#income
def income_create(request):
    form = IncomeForm()
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid:
            products = Product.objects.get(id=request.POST['product'])
            products.amount += int(request.POST['amount'])
            products.save()
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'income_create.html', context)


#history_expences
def current_product_ex(request, product_id):
    if request.method == 'POST':
        print(request.POST['id'])
    product = Outgoung.objects.filter(product_id=product_id).order_by('-added')
    context = {'current_product_ex': product}
    return render(request, 'product_ex.html', context)


# expence
def expence_create(request):
    form = ExpenceForm()
    if request.method == 'POST':
        form = ExpenceForm(request.POST)
        if form.is_valid:
            products = Product.objects.get(id=request.POST['product'])
            products.amount -= int(request.POST['amount'])
            products.save()
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'expence_create.html', context)


 # Register user
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page')

    context = {'form': form}
    return render(request, 'register.html', context)




# login
def login_check(request):
    form = LoginForm()
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('page')

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_check(request):
    logout(request)
    return redirect('page')