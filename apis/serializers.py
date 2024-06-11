from rest_framework import serializers  
from .models import Student

  

class StudentSerializer(serializers.ModelSerializer):  
    first_name = serializers.CharField(max_length=200, required=True)  
    last_name = serializers.CharField(max_length=200, required=True)  
    address = serializers.CharField(max_length=200, required=True)  
    roll_number = serializers.IntegerField()  
    mobile = serializers.CharField(max_length=10, required=True)  

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'address', 'roll_number', 'mobile']
        read_only_fields = ['id']

    # def create(self, validated_data):  

    #     """ 

    #     Create and return a new `Student` instance, given the validated data. 

    #     """  

    #     return Student.objects.create(**validated_data)  

  

    # def update(self, instance, validated_data):  

    #     """ 

    #     Update and return an existing `Student` instance, given the validated data. 

    #     """  

    #     instance.first_name = validated_data.get('first_name', instance.first_name)  
    #     instance.last_name = validated_data.get('last_name', instance.last_name)  
    #     instance.address = validated_data.get('address', instance.address)  
    #     instance.roll_number = validated_data.get('roll_number', instance.roll_number)  
    #     instance.mobile = validated_data.get('mobile', instance.mobile)  

    #     instance.save()  

    #     return instance 
