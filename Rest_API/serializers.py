from rest_framework import serializers
from .models import DataStock, DatewiseIndex
#django-rest-pandas  Pandas with Rest API 
class DataStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataStock
        fields = ['Symbol', 'Date','Open', 'High', 'Low', 'Close', 'Vol']


class DatewiseIndexSerializer(serializers.ModelSerializer):

        class Meta:
            model = DatewiseIndex
            fields = ['Date', 'NepseIndex']
            # fields = '__all__'