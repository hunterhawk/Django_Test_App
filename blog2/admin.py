from django.contrib import admin
from .models import Article, Person, UserInfo

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','pwd',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
