from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

class Coment(admin.StackedInline):
    model = CommentCrm
    dields = ('comment_text', 'comment_dt')
    readonly_fields = ('comment_dt',)
    extra = 1




class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_phone', 'order_name')
    list_display_links =  ('id', 'order_name')
    search_fields = ('id', 'order_status', 'order_phone', 'order_name')
    list_filter = ('id', 'order_status', 'order_phone', 'order_name')
    list_editable = ('order_status', 'order_phone')
    list_per_page = 10
    list_max_show_all = 100
    fealds = ('id', 'order_status', 'order_phone', 'order_dt')
    readonly_fields = ('id', 'order_dt')
    inlines = [Coment,]

admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
# Register your models here.
