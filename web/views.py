from django.shortcuts import render
from django.http import HttpResponse


def public_index(request):
   
    return render(request,'public/index.html')



def public_business(request):

    return render(request,'public/business.html')


    # from here some codes are directly copied

def campaigns(request):

    return render(request,'campaigns.html')


def campaign(request):
    return render(request,'campaign.html')

def profile(request):
    return render(request, 'profile.html')


def   public_campaigns(request):
    return render(request,'public/campaigns.html')



def campaign_view(request):
    return render(request,'shop/campaign.html')






def contact_us(request):

    context = {
        "title" : "Contact Us"
    }

    return render(request,'web/contact_us.html',context)


def privacy(request):
    context = {
        "title" : "Privacy Policy"
    }
    return render(request,'web/privacy.html',context)


def public_privacy(request):
    context = {
        "title" : "Privacy Policy"
    }
    return render(request,'web/public/privacy.html',context)


def support(request):
    context = {
        "title" : "Support"
    }
    return render(request,'web/support.html',context)


def public_support(request):
    context = {
        "title" : "Support"
    }
    return render(request,'web/public/support.html',context)


     