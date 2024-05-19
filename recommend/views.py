# recommend/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .recommendation_engine import get_association_rule_recommendations, get_collaborative_filtering_recommendations

def home(request):
    return render(request, 'home.html')

def new_user(request):
    recommendations = get_association_rule_recommendations("new_user")  
    return render(request, 'new_user.html', {'recommendations': recommendations})

def existing_users(request):
    # For demonstration, we'll use dummy user IDs. Replace with real user IDs from your data.
    user_ids = [1,
 2,
 2051,
 4101,
 2054,
 4102,
 2056,
 2059,
 12,
 13,
 4111,
 2064,
 8208,
 2069,]
    return render(request, 'existing_users.html', {'user_ids': user_ids})

def existing_user_recommendations(request, user_id):
    recommendations = get_collaborative_filtering_recommendations(user_id)
    return render(request, 'existing_user_recommendations.html', {'user_id': user_id, 'recommendations': recommendations})
