from django.urls import path, include
from .views import EmployeeList, EmployeeDetail, HashtagList, HashtagDetail, HashtagFilterAPIView,EmployeeFilterAPIView, PostList, PostDetail, EmployeeCreate
# Hashtagfilter,filterEmail,filterDelete,filterDate
from rest_framework import routers


urlpatterns = [
    path('Employee/',EmployeeList.as_view()),
    path('Employee/<int:pk>',EmployeeDetail.as_view()),
    path('Hashtag/',HashtagList.as_view()),
    path('Hashtag/<int:pk>',HashtagDetail.as_view()),
    path('Post/',PostList.as_view()),
    path('Post/<int:pk>',PostDetail.as_view()),
    # path('name/', Hashtagfilter.as_view()),
    # path('email/', filterEmail.as_view()),
    # path('delete/', filterDelete.as_view()),
    # path('date/', filterDate.as_view())
    path('hashtags/',HashtagFilterAPIView.as_view()),
    path('employees/',EmployeeFilterAPIView.as_view()),
]

router = routers.DefaultRouter()
router.register(r'createmp',EmployeeCreate,basename = 'create_emp')
urlpatterns+=router.urls
