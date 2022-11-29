from django.shortcuts import render

# Create your views here.

def master_home(request):
    return render(request,'master_templates/home.html')
def master_about(request):
    return render(request,'master_templates/about.html')
def master_blog(request):
    return render(request,'master_templates/blog.html')
def master_portfolio(request):
    return render(request,'master_templates/portfolio.html')
def master_contact(request):
    return render(request,'master_templates/contact.html')
