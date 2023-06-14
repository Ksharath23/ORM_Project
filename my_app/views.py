from rest_framework import generics,status,viewsets
from rest_framework.response import Response
from django.db.models import Q, F, Count
from django.shortcuts import get_object_or_404
# Create your views here.
import datetime
from .models import Employee, Hashtag, Post

from .serializers import EmployeeSerializer, HashtagSerializer, PostSerializer
from rest_framework.decorators import APIView
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


        filters = Q()

        name = self.request.query_params.get('name')
        if name:
            filters |= Q(name=name)

        email = self.request.query_params.get('email')
        if email:
            filters |= Q(email=email)

        created_at = self.request.query_params.get('created_at')
        if created_at:
            date = datetime.datetime.strptime(created_at, "%Y-%m-%d")
            filters |= Q(created_at__gt=date)

        is_delete = self.request.query_params.get('is_delete')
        if is_delete:
            filters |= Q(is_delete=is_delete)
        
        created_by = self.request.query_params.get('created_by')
        if created_by:
            filters |= Q(created_by=created_by)

        if filters:
            queryset = queryset.filter(filters)
        print("query_set:",queryset)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"result": serializer.data})
        # return Response({"result": queryset})

        # name = self.request.query_params.get('name')
        # if name:
        #     queryset = queryset.filter(name__icontains=name)

        # email = self.request.query_params.get('email')
        # if email:
        #     queryset = queryset.filter(created_by__email=email)

        # created_at = self.request.query_params.get('created_at')
        # if created_at:
        #     date = datetime.datetime.strptime(created_at, "%Y-%m-%d")
        #     queryset = queryset.filter(created_at__gt=date)

        # is_delete = self.request.query_params.get('is_delete')
        # if is_delete:
        #     queryset = queryset.filter(is_delete=is_delete)
        
        # created_by = self.request.query_params.get('created_by')
        # print(created_by)
        # if created_by:
        #     queryset = queryset.filter(created_by__user__username=created_by)
        # print("query_Set",queryset)
        # return queryset

class PostFilterAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset = Post.objects.all()


        filters = Q()

        post_name = self.request.query_params.get('post_name')
        
        created_by = self.request.query_params.get('created_by')

        hashtag = self.request.query_params.get('hashtag')

        is_delete = self.request.query_params.get('is_delete')

        if created_by:
            filters &= Q(created_by__user__username=created_by)
        
        if hashtag:
            filters &= Q(hashtag__name=hashtag)

        if post_name:
            filters &= Q(post_name=post_name)
        #     queryset = queryset.annotate(name = F('created_by__user__username'),email_id = F('created_by__user__email')).values('name','email_id')

        if is_delete:
            filters &= Q(is_delete=is_delete)

        if filters:
            queryset = queryset.filter(filters).annotate(name=F('created_by__user__username'),email_id = F('created_by__user__email'),hashtag_name= F('hashtag__name')).values()
        print("query_set:",queryset)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # serializer = self.get_serializer(queryset, many=True)
        # return Response({"result": serializer.data})
        return Response({"result": queryset})
    

# class PostAPIView(APIView):
#     def post(self,request):
#         post_name = self.request.query_params.get('post_name')
#         hashtag = self.request.query_params.get('hashtag')
#         created_by = self.request.query_params.get('created_by')
#         created_at = self.request.query_params.get('created_at')
#         description = self.request.query_params.get('description')
#         caption =  self.request.query_params.get('caption')
#         is_delete = self.request.query_params.get('is_delete','')
    
#         object = Post.objects.create(post_name=post_name,hashtag=hashtag,created_by=created_by,created_at=created_at,description=description,caption=caption,is_delete=is_delete)
    
class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request):
        try:
            post = Post.objects.get(id=request.data['id'])
        except Post.DoesNotExist:
            return Response({'error': 'Post does not exist.'})
        
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PostNewView(APIView):
    def get(self,request):
        posts = Post.objects.all()
        data = []
        for post in posts:
            post_data = {
                'id': post.id,
                'post_name': post.post_name,
                'hashtag': [hashtag.id for hashtag in post.hashtag.all()],
                'created_by': post.created_by.id,
                'created_at': post.created_at,
                'description': post.description,
                'caption': post.caption,
                'is_delete': post.is_delete
            }
            data.append(post_data)
        return Response(data)

    def post(self, request):
        # import pdb; pdb.set_trace()
        post_data = {
           
            'post_name': request.data.get('post_name'),
            # 'hashtag': request.data.get('hashtag'),
            'created_at': request.data.get('created_at'),
            # 'created_by_id':request.data.get('created_by'),
            'description': request.data.get('description'),
            'caption': request.data.get('caption'),
            'is_delete': request.data.get('is_delete')
        }
        # employee_id = request.data.get('created_by')    
        # try:
        #     employee = Employee.objects.get(employee_id=employee_id)
        # except Employee.DoesNotExist:
        #     return Response({'error': 'Employee does not exist.'})
        # post_data['created_by'] = employee

        hashtag = request.data.get('hashtag')

        post = Post.objects.create(**post_data)
        post.hashtag.add(*hashtag)
        return Response({"post created":"success"})
    
    def put(self, request, format=None):
        post_id = request.data.get('id')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post does not exist.'})
        
        post.post_name = request.data.get('post_name')
        post.description = request.data.get('description')
        post.caption = request.data.get('caption')
        post.is_delete = request.data.get('is_delete')
        created_by = request.data.get('created_by')
        # import pdb; pdb.set_trace()
        if created_by:
            try:
                post.created_by = Employee.objects.get(id=created_by)
            except Employee.DoesNotExist:
                pass

        hashtag_ids = request.data.get('hashtag')
        if hashtag_ids:
            post.hashtag.clear()
            for hashtag_id in hashtag_ids:
                try:
                    hashtag = Hashtag.objects.get(id=hashtag_id)
                    post.hashtag.add(hashtag)
                except Hashtag.DoesNotExist:
                    pass
        
        
        post.save()
        
        return Response({"put updated":"success"})