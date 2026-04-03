from django.contrib import admin

from d_student . models import Student_detail



# admin.site.register(Student_detail)

@admin.register(Student_detail)

class StudentAdmin(admin.ModelAdmin):

    list_display=('name',"age","city")
    search_fields=('name','age','city')
    list_filter=('age','city')
    ordering=('name',)


