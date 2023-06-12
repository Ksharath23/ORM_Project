from django.urls import path
from .views import EmployeeList, EmployeeDetail, HashtagList, HashtagDetail, HashtagFilterAPIView,EmployeeFilterAPIView
# Hashtagfilter,filterEmail,filterDelete,filterDate


urlpatterns = [
    path('Employee/',EmployeeList.as_view()),
    path('Employee/<int:pk>',EmployeeDetail.as_view()),
    path('Hashtag/',HashtagList.as_view()),
    path('Hashtag/<int:pk>',HashtagDetail.as_view()),
    # path('name/', Hashtagfilter.as_view()),
    # path('email/', filterEmail.as_view()),
    # path('delete/', filterDelete.as_view()),
    # path('date/', filterDate.as_view())
    path('hashtags/',HashtagFilterAPIView.as_view()),
    path('employees/',EmployeeFilterAPIView.as_view())
]

