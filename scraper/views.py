from django.shortcuts import render

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from rest_framework.decorators import api_view
from uritemplate import partial
from .serializers import *

from . models import *






from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@api_view(['POST'])
def NameCheap(request):

        if request.method == "POST":

            serializer = Name_Cheap_Serializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()
        url = serializer.data.get("url")
        driver = Chrome(executable_path = "C:/Users/shaphat/Desktop/PROJECTS/FUN PROJECTS/domain_search/scraper/chromedriver.exe")
        driver.get(f'{url}')
        delay = 120

        try:
            data = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, 'price')))


            print(data.text)
            
            #print(price.text)
        except TimeoutException:
            print ("Loading took too much time!")

        


        return Response(f'"{data.text}"')




@api_view(['POST'])
def Domain(request):

        if request.method == "POST":

            serializer = DomainSerializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()
        url = serializer.data.get("url")
        driver = Chrome(executable_path = "C:/Users/shaphat/Desktop/PROJECTS/FUN PROJECTS/domain_search/scraper/chromedriver.exe")
        driver.get(f'{url}')
        delay = 120

        try:
            data = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, 'cart-total')))


            print(data.text)
            
            #print(price.text)
        except TimeoutException:
            print ("Loading took too much time!")

        


        return Response(f'"{data.text}"')




@api_view(['POST'])
def Hover(request):

        if request.method == "POST":

            serializer = HoverSerializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()
        url = serializer.data.get("url")
        driver = Chrome(executable_path = "C:/Users/shaphat/Desktop/PROJECTS/FUN PROJECTS/domain_search/scraper/chromedriver.exe")
        driver.get(f'{url}')
        delay = 120

        try:
            data = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, 'price')))


            print(data.text)
            
            #print(price.text)
        except TimeoutException:
            print ("Loading took too much time!")

        


        return Response(f'"{data.text}"')
        

