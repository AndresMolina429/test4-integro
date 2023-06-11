from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from .logic import Test4Logic
import json

# Create your views here.
class Test4View(View, Test4Logic):
    def get_context_data(self):
        body = json.loads(self.request.body)
        phrase = body['phrase']
        return self.is_palindrome(phrase)


    def post(self, request, *args, **kwargs):
        response = HttpResponse()
        response["X-Frame-Options"] = "SAMEORIGIN"
        return JsonResponse(self.get_context_data())
        # return self.get_context_data()
