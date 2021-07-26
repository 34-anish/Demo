from django.http.response import HttpResponse
from django.shortcuts import render
from .models import DataStock, DatewiseIndex

import pandas as pd


from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataStockSerializer, DatewiseIndexSerializer


import json
# Create your views here.

#Class based views
#Function based views

class DataStockList(APIView):
    
    def get(self, request):
        symb = "ACEDBL"
        # symb = request.GET.get('stock_symbol')
        stock = DataStock.objects.filter(Symbol=symb).reverse()[700:]

        serializer = DataStockSerializer(stock, many=True)
        return Response(serializer.data)


    def post(self):
        pass


class DataStockList2(APIView):
    
    def get(self, request, stock_symbol):
        # symb = "ACEDBL"
        symb = stock_symbol
        # symb = request.GET.get('stock_symbol')
        # stock = DataStock.objects.filter(Symbol=symb).reverse()[800:]
        stock = DataStock.objects.filter(Symbol=symb).order_by('-Date')[0:60]
        # print(stock.values())
        df = pd.DataFrame(stock.values())
        print(df)
        serializer = DataStockSerializer(stock, many=True)
        return Response(serializer.data)


    def post(self):
        pass


class DatewiseIndexList(APIView):
    
    def get(self, request):
        d_index = DatewiseIndex.objects.all()
        serializer = DatewiseIndexSerializer(d_index, many=True)
        return Response(serializer.data)


    def post(self):
        pass
 
