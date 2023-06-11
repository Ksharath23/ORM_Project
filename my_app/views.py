from rest_framework import generics,status
from rest_framework.response import Response
# Create your views here.
import datetime
from .models import Employee, Hashtag

from .serializers import EmployeeSerializer, HashtagSerializer

class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class HashtagList(generics.ListCreateAPIView):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()

class HashtagDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()

class HashtagList(generics.ListCreateAPIView):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()

class Hashtagfilter(generics.ListAPIView):
    serializer_class = HashtagSerializer

    def list(self,request):
        name =  self.request.query_params.get('name') 
        query = Hashtag.objects.filter(name__icontains = name)
        serializer = self.get_serializer(query,many=True)
        return Response({"result":serializer.data})
    
class filterEmail(generics.ListAPIView):
    serializer_class = HashtagSerializer

    def get_queryset(self,request):
        email = self.query_params.get('email')
        query = Hashtag.objects.filter(created_by__email = email)
        # serializer = self.get_serializer(query,many=True)
        # return Response({"result:":serializer.data})
        return query

class filterDate(generics.ListAPIView):
    serializer_class = HashtagSerializer

    def list(self,request):
        created_at = self.request.query_params.get("created_at")
        date = datetime.datetime.strptime(created_at,"%Y-%m-%d")
        query = Hashtag.objects.filter(created_at__gt = date)
        serializer = self.get_serializer(query,many=True)
        return Response({"result":serializer.data})

class filterDelete(generics.ListAPIView):
    serializer_class = HashtagSerializer

    def list(self,request):
        is_delete = self.request.query_params.get("is_delete")
        print("is_delete",is_delete)
        query = Hashtag.objects.filter(is_delete = is_delete)
        serializer = self.get_serializer(query,many=True)
        return Response({"result":serializer.data})