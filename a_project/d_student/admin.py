from django.contrib import admin

from d_student . models import Student_detail,Department



# admin.site.register(Department)


# @admin.register(Department)

# class DepartmentAdmin(admin.ModelAdmin):
#     list_display=('d_name',)
#     search_fields=('name',)

@admin.register(Student_detail)

class StudentAdmin(admin.ModelAdmin):
    list_display=('name',"age","city")
    search_fields=('name','age','city')
    list_filter=('age','city')
    ordering=('name',)
@admin.register(Department)
class DepratmentAdmin(admin.ModelAdmin):
    list_display=('dep_name',)


