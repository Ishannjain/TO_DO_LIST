from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
# Create your views here.
def check(password):
    if len(password) < 8:
        return False
    isUpper = False
    isLower = False
    isDigit = False
    for ch in password:
        if ch.isupper():
            isUpper = True
        if ch.islower():
            isLower = True
        if ch.isdigit():
            isDigit = True
    
    return isUpper and isLower and isDigit
def index(request):
    return render(request,'task/index.html')
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', '')
            if next_url:
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "task/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "task/login.html", {
            "next": request.GET.get('next', '')
        })
    
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if not check(password):
                    return render(request, "task/register.html", {
                        "message": "Passwords does not meet requirements. Minimun length 8 and should contain atleast one Capital Letter, one small Letter and one digit"
                    })

        if password != confirmation:
            return render(request, "task/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "task/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "task/register.html")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
from django.db.models import Q

def display_listing(request):
    # Start with the base queryset
    listings = Listing.objects.filter(isActive=True, user=request.user)

    # Filtering by search term (if provided)
    search_term = request.GET.get('search', '')
    if search_term:
        listings = listings.filter(Q(role__icontains=search_term))

    # Filtering by priority (if provided)
    priority = request.GET.get('priority', '')
    if priority:
        listings = listings.filter(Priority=priority)

    # Filtering by date range (if provided)
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    if start_date and end_date:
        listings = listings.filter(start_date__gte=start_date, end_date__lte=end_date)

    # Sorting by due date and priority
    listings = listings.order_by('end_date', 'Priority')

    return render(request, 'task/display_listing.html', {'listings': listings})



@login_required
def create_listing(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        priority = request.POST.get('priority')
        start_date = parse_date(request.POST.get('start_date'))
        end_date = parse_date(request.POST.get('end_date'))
        role = request.POST.get('role')
        is_active = request.POST.get('isActive') == 'on'

        category = Category.objects.get(id=category_id)

        listing = Listing.objects.create(
            user=request.user,
            category=category,
            Priority=priority,
            start_date=start_date,
            end_date=end_date,
            role=role,
            isActive=is_active
        )
        return redirect('display_listing')  # or wherever you want to redirect

    categories = Category.objects.filter(user=request.user)
    return render(request, 'task/create_listing.html', {'categories': categories})
@login_required
def edit_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id, user=request.user)
    if request.method == 'POST':
        category_id = request.POST.get('category')
        listing.category = Category.objects.get(id=category_id)
        listing.Priority = request.POST.get('priority')
        listing.start_date = parse_date(request.POST.get('start_date'))
        listing.end_date = parse_date(request.POST.get('end_date'))
        listing.role = request.POST.get('role')
        listing.isActive = request.POST.get('isActive') == 'on'
        listing.save()
        return redirect('display_listing')

    categories = Category.objects.filter(user=request.user)
    return render(request, 'task/edit_listing.html', {
        'listing': listing,
        'categories': categories
    })
@login_required
def delete_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id, user=request.user)
    if request.method == 'POST':
        listing.delete()
        return redirect('display_listing')
    return render(request, 'task/delete_listing.html', {'listing': listing})

        
def categories_list(request):
    if request.method=='POST':
        name=request.POST.get('name')
        if name:
            Category.objects.create(
                name=name,
                user=request.user
                )
            return redirect('categories_list')
    categories=Category.objects.filter(user=request.user)
    return render(request,'task/categories_list.html',{
        "categories":categories
    })