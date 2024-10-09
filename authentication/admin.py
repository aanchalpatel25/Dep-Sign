from django.contrib import admin
from authentication.models import detail, answer,question


class answeradmin(admin.ModelAdmin):
    list_display = ['username', 'answer1', 'answer2', 'answer3', 'answer4',
                    'answer5', 'answer6', 'answer7', 'answer8', 'answer9', 'answer10', 'date','result' ]


class detailadmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'username']


class questionadmin(admin.ModelAdmin):
    list_display = ['id','questions']


# Register your models here.
admin.site.register(answer, answeradmin)
admin.site.register(detail, detailadmin)
admin.site.register(question, questionadmin)
