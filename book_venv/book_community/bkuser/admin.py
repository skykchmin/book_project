from django.contrib import admin
from .models import Bkuser
# Register your models here.
class BkuserAdmin(admin.ModelAdmin):
   list_display = ('username', 'password') # 웹상에서 출력하고 싶은 필드들을 보여준다

admin.site.register(Bkuser, BkuserAdmin)