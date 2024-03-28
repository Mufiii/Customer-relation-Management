from rest_framework import serializers
from .models import Leed


class LeedListSerializer(serializers.ModelSerializer):

    class Meta:
      model = Leed
      fields = '__all__'
      

class LeedsPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leed
        fields = [
          'company_name','salutation','first_name','last_name','email','phone','country',
          'state','city','executive','designation','product','requirement','notes'
        ]