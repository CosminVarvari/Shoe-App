import json

from django.shortcuts import render, redirect
import xml.etree.ElementTree as ET
import csv
import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .models import Product
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
# Create your views here.

@api_view(['GET','POST'])
def add_products(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def view_products(request):
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT', 'DELETE'])
def detail_product(request, pk):
    try:
        products = Product.objects.get(pk = pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        pass
    elif request.method == 'GET':
        serializer = ProductSerializer(products)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        pass


@api_view(['GET','PUT', 'DELETE'])
def update_product(request):
    try:
        id = request.data["id"]
        product = Product.objects.get(pk = id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass


@api_view(['GET','PUT', 'DELETE'])
def delete_product(request, pk):
    try:
        products = Product.objects.get(pk = pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        pass
    elif request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == 'sort by price' and request.user.is_employee:
            products = Product.objects.order_by('price')
            return render(request, 'searchbar.html', {'products': products})
        elif query == 'sort by store' and request.user.is_manager:
            products = Product.objects.order_by('store')
            return render(request, 'searchbar.html', {'products': products})
        elif query == 'available products':
            products = Product.objects.filter(is_available='True')
            return render(request, 'searchbar.html', {'products': products})
        elif query == 'not available products':
            products = Product.objects.filter(is_available='False')
            return render(request, 'searchbar.html', {'products': products})
        elif query.isnumeric():
            products = Product.objects.filter(price=query)
            return render(request, 'searchbar.html', {'products': products})
        elif query == 'Gucci':
            products = Product.objects.filter(producer=4)
            return render(request, 'searchbar.html', {'products': products})
        elif query == 'Adidas':
            products = Product.objects.filter(producer=2)
            return render(request, 'searchbar.html', {'products': products})
        elif query == 'Nike':
            products = Product.objects.filter(producer=1)
            return render(request, 'searchbar.html', {'products': products})
        elif query == 'Puma':
            products = Product.objects.filter(producer=3)
            return render(request, 'searchbar.html', {'products': products})
        elif query and request.user.is_employee:
            products = Product.objects.filter(name=query)
            return render(request, 'searchbar.html', {'products': products})
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})


def export_csv_employee(request):
    file_path = os.path.join(settings.BASE_DIR, 'Files', 'situatia_produselor-employee.csv')
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Store', 'Price', 'Description', 'is_available', 'created_at', 'producer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        products = Product.objects.all()
        for product in products:
            writer.writerow({'Name': product.name, 'Store': product.store, "Price": product.price,
                             'Description': product.description, 'is_available': product.is_available,
                             'created_at': product.created_at, 'producer': product.producer})
    return HttpResponse('CSV file created successfully.')


def export_json_employee(request):
    file_path = os.path.join(settings.BASE_DIR, 'Files', 'situatia_produselor-employee.json')
    products = Product.objects.filter(store=1)

    # Build a list of dictionaries representing the products
    product_list = []
    for product in products:
        product_dict = {
            'Name': product.name,
            'Store': product.store.name,
            'Price': float(product.price),
            'Description': product.description,
            'is_available': product.is_available,
            'created_at': product.created_at.strftime("%d-%m-%Y"),
            'producer': product.producer.name
        }
        product_list.append(product_dict)

    # Write the product list to the JSON file
    with open(file_path, 'w') as jsonfile:
        json.dump(product_list, jsonfile)

    return HttpResponse('JSON file created successfully.')


def export_txt_employee(request):
    file_path = os.path.join(settings.BASE_DIR, 'Files', 'situatia_produselor-employee.txt')
    with open(file_path, 'w') as txtfile:
        products = Product.objects.filter(store=1)
        for product in products:
            txtfile.write(
                f"Name: {product.name}\nStore: {product.store}\nPrice: {product.price}\nDescription: {product.description}\nis_available: {product.is_available}\ncreated_at: {product.created_at}\nproducer: {product.producer}\n\n")
    return HttpResponse('TXT file created successfully.')


def export_xml_employee(request):
    file_path = os.path.join(settings.BASE_DIR, 'Files', 'situatia_produselor-employee.xml')

    # Create the root element
    root = ET.Element('products')

    products = Product.objects.filter(store=1)
    for product in products:
        # Create a new product element
        product_elem = ET.SubElement(root, 'product')

        # Add the product attributes as subelements
        ET.SubElement(product_elem, 'name').text = str(product.name)
        ET.SubElement(product_elem, 'store').text = str(product.store)
        ET.SubElement(product_elem, 'price').text = str(product.price)
        ET.SubElement(product_elem, 'description').text = str(product.description)
        ET.SubElement(product_elem, 'is_available').text = str(product.is_available)
        ET.SubElement(product_elem, 'created_at').text = str(product.created_at)
        ET.SubElement(product_elem, 'producer').text = str(product.producer)

    # Write the XML data to the file
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

    return HttpResponse('XML file created successfully.')


def export_csv_manager(request):
    file_path = os.path.join(settings.BASE_DIR, 'Files', 'situatia_produselor-manager.csv')
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Store', 'Price', 'Description', 'is_available', 'created_at', 'producer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        products = Product.objects.all()
        for product in products:
            writer.writerow({'Name': product.name, 'Store': product.store, "Price": product.price,
                             'Description': product.description, 'is_available': product.is_available,
                             'created_at': product.created_at, 'producer': product.producer})
    return HttpResponse('CSV file created successfully.')


def export_json_manager(request):
    file_path = os.path.join(settings.BASE_DIR, 'Files', 'situatia_produselor-manager.json')
    products = Product.objects.all()

    # Build a list of dictionaries representing the products
    product_list = []
    for product in products:
        product_dict = {
            'Name': product.name,
            'Store': product.store.name,
            'Price': float(product.price),
            'Description': product.description,
            'is_available': product.is_available,
            'created_at': product.created_at.strftime("%d-%m-%Y"),
            'producer': product.producer.name
        }
        product_list.append(product_dict)

    # Write the product list to the JSON file
    with open(file_path, 'w') as jsonfile:
        json.dump(product_list, jsonfile)

    return HttpResponse('JSON file created successfully.')


def export_txt_manager(request):
    file_path = os.path.join(settings.BASE_DIR, 'Files', 'situatia_produselor-manager.txt')
    with open(file_path, 'w') as txtfile:
        products = Product.objects.all()
        for product in products:
            txtfile.write(
                f"Name: {product.name}\nStore: {product.store}\nPrice: {product.price}\nDescription: {product.description}\nis_available: {product.is_available}\ncreated_at: {product.created_at}\nproducer: {product.producer}\n\n")
    return HttpResponse('TXT file created successfully.')


def export_xml_manager(request):
    file_path = os.path.join(settings.BASE_DIR, 'Files', 'situatia_produselor-manager.xml')

    # Create the root element
    root = ET.Element('products')

    products = Product.objects.all()
    for product in products:
        # Create a new product element
        product_elem = ET.SubElement(root, 'product')

        # Add the product attributes as subelements
        ET.SubElement(product_elem, 'name').text = str(product.name)
        ET.SubElement(product_elem, 'store').text = str(product.store)
        ET.SubElement(product_elem, 'price').text = str(product.price)
        ET.SubElement(product_elem, 'description').text = str(product.description)
        ET.SubElement(product_elem, 'is_available').text = str(product.is_available)
        ET.SubElement(product_elem, 'created_at').text = str(product.created_at)
        ET.SubElement(product_elem, 'producer').text = str(product.producer)

    # Write the XML data to the file
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

    return HttpResponse('XML file created successfully.')


def pie_chart(request):
    labels = []
    data = []

    queryset = Product.objects.order_by('price')[:5]
    for product in queryset:
        labels.append(product.name)
        data.append(int(product.price))
    print(labels, data)
    return render(request,'statistics.html', {
        'labels': labels,
        'data': data
    })

def bar_chart(request):
    labels = []
    data = []

    queryset = Product.objects.order_by('price')[:5]
    for product in queryset:
        labels.append(product.name)
        data.append(int(product.price))
    print(labels, data)
    return render(request,'barChart.html', {
        'labels': labels,
        'data': data
    })

def line_chart(request):
    labels = []
    data = []

    queryset = Product.objects.order_by('price')[:5]
    for product in queryset:
        labels.append(product.name)
        data.append(int(product.price))
    print(labels, data)
    return render(request,'lineChart.html', {
        'labels': labels,
        'data': data
    })



def switch_mng(request, lang):
    if request.POST.get('Ro'):
        lang = 'ro'
    if request.POST.get('En'):
        lang = 'en-us'
    if request.POST.get('Es'):
        lang='es'
    return lang


def switch_emp(request, lang):
    if request.POST.get('Ro'):
        lang = 'ro'
    if request.POST.get('En'):
        lang = 'en-us'
    if request.POST.get('Es'):
        lang='es'
    return lang