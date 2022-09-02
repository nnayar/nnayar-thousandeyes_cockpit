from django.shortcuts import render
from django.http import HttpResponse
import requests
from test_management.thousandeyesapi import ThousandEyesApi
import json

# Create your views here.
def tests(request):
    te = ThousandEyesApi()
    resp = te.getRequest('/tests')
    list_of_tests_json = resp.json()
    return render(request, "tests.html", {'tests' : list_of_tests_json['test']})
