from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from writer.models import Article

from .models import Subscription


@login_required(login_url='my-login')
def client_dashboard(request):
    try:
        subDetails = Subscription.objects.get(user=request.user)
        subscription_plan = subDetails.subscription_plan

        context = {
            'subscription_plan': subscription_plan,
        }
        return render(request, 'client/client-dashboard.html', context)
    except Subscription.DoesNotExist:
        subscription_plan = None
        context = {
            'subscription_plan': subscription_plan,
        }
        return render(request, 'client/client-dashboard.html', context)


@login_required(login_url='my-login')
def browse_articles(request):

    try:
        subDetails = Subscription.objects.get(user=request.user, is_active=True)
    except Subscription.DoesNotExist:
        return render(request, 'client/subscription-locked.html')
    
    current_subscription_plan = subDetails.subscription_plan
    if current_subscription_plan == 'standard':
        articles = Article.objects.all().filter(is_premium=False)
    elif current_subscription_plan == 'premium':
        articles = Article.objects.all()

        # context Django view-এর একটা খুব গুরুত্বপূর্ণ অংশ। সহজভাবে বললে, context হলো data container (ডাটা পাঠানোর মাধ্যম) — যেটা দিয়ে backend (view) থেকে frontend (template)-এ ডাটা পাঠানো হয়।

    context = {
        'AllClientArticles': articles,
    }

    return render(request, 'client/browse-articles.html', context)


@login_required(login_url='my-login')
def subscription_locked(request):
    return render(request, 'client/subscription-locked.html')