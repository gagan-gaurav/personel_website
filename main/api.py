import json
from django.http import JsonResponse
from django.core import serializers
from .models import (
	UserProfile,
	Portfolio)

def apiUserDetails(request):
	body = serializers.serialize("json", UserProfile.objects.all())
	return JsonResponse({'body' : body, 'success': True})

def apiPortfolioDetails(request):
	body = serializers.serialize("json", Portfolio.objects.all())
	return JsonResponse({'body' : body, 'success': True})