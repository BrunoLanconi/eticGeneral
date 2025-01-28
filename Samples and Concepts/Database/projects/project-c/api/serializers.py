from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from api.models import Product


class ProductSerializer(ModelSerializer):
    evil_name = SerializerMethodField()
  
  
    class Meta:
        model = Product
        fields = ("id", "name", "evil_name")
        
    def get_evil_name(self, obj):
        return obj.name + " is evil"
