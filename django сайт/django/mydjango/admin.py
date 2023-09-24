from django.contrib import admin
from .models import Posting
from .models import Feedback

admin.site.register(Posting)


class PostAdmin(admin.ModelAdmin):
    # Добавим в начало столбец pk
    list_display = ('pk', 'text', 'pub_date', 'author') 
    search_fields = ('text',) 
    list_filter = ('pub_date',) 


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']

admin.site.register(Feedback, FeedbackAdmin)