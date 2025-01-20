from django.template.defaultfilters import title
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = "__all__"









# def encode():
#     model = WomenModel('pididi', 'content: pididi')
#     model.sr = WomenSerializer(model)
#     print(model.sr.data, type(model.sr.data), sep='\n')
#     json = JSONRenderer().render(model.sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"pididi", "content":"Content: pididi"}')
#     data = JSONParser().parse(stream)
#     serializers = WomenSerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)