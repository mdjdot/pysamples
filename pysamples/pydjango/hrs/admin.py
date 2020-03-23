from django.contrib import admin
from hrs.models import Dept
from hrs.models import Emp

# Register your models here.


class DeptAdmin(admin.ModelAdmin):
    list_display = ('no',  'name', 'location')
    ordering = ('no',)


class EmpAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'title', 'mgr', 'salary', 'subsidy', 'dept')
    search_fields = ('name', 'title')


admin.site.register(Dept, DeptAdmin)
admin.site.register(Emp, EmpAdmin)
