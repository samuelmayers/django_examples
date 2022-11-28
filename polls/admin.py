from django.contrib import admin
from .models import Question, Choice

class Choiceinline(admin.StackedInline):
    model= Choice
    extra = 3

class QuetionAdmin(admin.ModelAdmin):
    fields = ["question_text"]
    inlines = [Choiceinline]
    list_display= ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields=['question_text']


admin.site.register(Question,QuetionAdmin)


