from django.contrib import admin
from .models import Test1User,Test1User,Location,LostItem,FoundItem,QRCode,Message,Notification,Rating,AdminLog

# Register your models here.
admin.site.register(Test1User)
admin.site.register(Location)
admin.site.register(LostItem)
admin.site.register(FoundItem)
admin.site.register(QRCode)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Rating)
admin.site.register(AdminLog)