from django.contrib import admin
from .models import BookInfo,HeroInfo
"""
django自带强大的后台管理
"""
# Register your models here.

class HeroInfoInlines(admin.StackedInline):
    model = HeroInfo
    extra = 1
class BookInfoAdmin(admin.ModelAdmin):
    # 重写list_display 重写后台显示哪些字段
    list_display = ("title", "pub_date")
    list_filter = ("title","pub_date")
    list_per_page = 20
    inlines = [HeroInfoInlines]
# 在注册模型时 注册该模型的后台管理类  通过管理类重写后台
admin.site.register(BookInfo,BookInfoAdmin)

class HeroInfoAdmin(admin.ModelAdmin):
    # list_display = ("name","content","skill")
    list_display = ("name", "content",)
    list_filter = ("name", )
    search_fields = ("name","content")
admin.site.register(HeroInfo,HeroInfoAdmin)

