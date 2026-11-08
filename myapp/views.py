# myapp/views.py
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile

# 1. Serves your traditional index.html frontend page
def home_page(request):
    return render(request, 'index.html')

# 2. Handles the async form data submission from your frontend main.js file
@csrf_exempt  # Bypasses session token checks for simple fetch() endpoint development testing
def register_user_api(request):
    if request.method == 'POST':
        try:
            # Parse the incoming stringified JSON array sent by JavaScript
            data = json.loads(request.body)
            name_input = data.get('name')
            email_input = data.get('email')

            if not name_input or not email_input:
                return JsonResponse({"error": "Please provide both a name and an email address."}, status=400)

            # Check if this email is already registered inside MongoDB
            if UserProfile.objects.filter(email=email_input).exists():
                return JsonResponse({"error": "This email address is already registered."}, status=400)

            # Securely insert the structural data layout into your cloud MongoDB instance
            new_record = UserProfile.objects.create(name=name_input, email=email_input)

            return JsonResponse({
                "message": "Success! Securely stashed in MongoDB Atlas.",
                "id": str(new_record.id)
            }, status=201)

        except Exception as error:
            return JsonResponse({"error": f"Internal database error: {str(error)}"}, status=500)

    return JsonResponse({"error": "Invalid request protocol method type."}, status=405)

