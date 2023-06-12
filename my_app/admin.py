from django.contrib import admin
from .models import Employee, Hashtag,Post
# Register your models here.
admin.site.register(Employee)
admin.site.register(Hashtag)
admin.site.register(Post)