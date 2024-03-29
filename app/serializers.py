from rest_framework import serializers
from app.models import *
class Productmodel(serializers.ModelSerializer):
    class Meta:
        models=Product
        field='__all__'