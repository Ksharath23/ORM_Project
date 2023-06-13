from rest_framework import generics,status,viewsets
from rest_framework.response import Response
from django.db.models import Q, F, Count
from django.shortcuts import get_object_or_404
# Create your views here.
import datetime
from .models import Employee, Hashtag, Post

from .serializers import EmployeeSerializer, HashtagSerializer, PostSerializer

class EmployeeCreate(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



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

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# class Hashtagfilter(generics.ListAPIView):
#     serializer_class = HashtagSerializer

#     def list(self,request):
#         name =  self.request.query_params.get('name') 
#         query = Hashtag.objects.filter(name__icontains = name)
#         serializer = self.get_serializer(query,many=True)
#         return Response({"result":serializer.data})
    
# class filterEmail(generics.ListAPIView):
#     serializer_class = HashtagSerializer

#     def get_queryset(self,request):
#         email = self.query_params.get('email')
#         query = Hashtag.objects.filter(created_by__email = email)
#         # serializer = self.get_serializer(query,many=True)
#         # return Response({"result:":serializer.data})
#         return query

# class filterDate(generics.ListAPIView):
#     serializer_class = HashtagSerializer

#     def list(self,request):
#         created_at = self.request.query_params.get("created_at")
#         date = datetime.datetime.strptime(created_at,"%Y-%m-%d")
#         query = Hashtag.objects.filter(created_at__gt = date)
#         serializer = self.get_serializer(query,many=True)
#         return Response({"result":serializer.data})

# class filterDelete(generics.ListAPIView):
#     serializer_class = HashtagSerializer

#     def list(self,request):
#         is_delete = self.request.query_params.get("is_delete")
#         print("is_delete",is_delete)
#         query = Hashtag.objects.filter(is_delete = is_delete)
#         serializer = self.get_serializer(query,many=True)
#         return Response({"result":serializer.data})

# class HashtagFilterAPIView(generics.ListAPIView):
#     serializer_class = HashtagSerializer

#     def get_queryset(self):
#         query_set = Hashtag.objects.all()

#         name = self.request.query_params.get('name')

class EmployeeFilterAPIView(generics.ListAPIView):
    serializer_class= EmployeeSerializer

    def get_queryset(self):
        query_set = Employee.objects.all()

        # first_name = self.request.query_params.get('first_name')
        # last_name = self.request.query_params.get('last_name')
        # if first_name:
        #     query_set = query_set.filter(Q(first_name=first_name)| Q(last_name=last_name))

        # employee_id = self.request.query_params.get('employee_id')
        # print(employee_id)
        # if employee_id:
        #     query_set = query_set.filter(employee_id=employee_id)
        #     print(query_set)
        #     query_set = query_set.annotate(name = F('user__username'),email_id = F('user__email')).values('name','email_id')
        #     print("query_set:",query_set)        
        # return query_set
        filters = Q()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        if first_name and last_name:
            filters |= Q(first_name=first_name)
            filters |= Q(last_name = last_name)

        employee_id = self.request.query_params.get('employee_id')

        if employee_id:
            filters &= Q(employee_id=employee_id)
            query_set = query_set.annotate(name = F('user__username'),email_id = F('user__email')).values('name','email_id')

        if filters:
            query_set = query_set.filter(filters)
        return query_set





            
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data)
        return Response({"result": serializer.data})
        # return Response({"result": queryset})

        


class HashtagFilterAPIView(generics.ListAPIView):
    serializer_class = HashtagSerializer

    def get_queryset(self):
        queryset = Hashtag.objects.all()

        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        email = self.request.query_params.get('email')
        if email:
            queryset = queryset.filter(created_by__email=email)

        created_at = self.request.query_params.get('created_at')
        if created_at:
            date = datetime.datetime.strptime(created_at, "%Y-%m-%d")
            queryset = queryset.filter(created_at__gt=date)

        is_delete = self.request.query_params.get('is_delete')
        if is_delete:
            queryset = queryset.filter(is_delete=is_delete)
        
        created_by = self.request.query_params.get('created_by')
        print(created_by)
        if created_by:
            queryset = queryset.filter(created_by__user__username=created_by)
        print("query_Set",queryset)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"result": serializer.data})
        # return Response({"result": queryset})
    