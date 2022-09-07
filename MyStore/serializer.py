from rest_framework import serializers
from .models import Store
# class StoreSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)  
#     image= serializers.URLField(max_length=200)
#     stock=serializers.IntegerField(default=0)
#     price= serializers.IntegerField(default=0)
#     discount= serializers.IntegerField(default=0)

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name','image','stock','price','discount')