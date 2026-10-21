
from django.contrib import admin
from classschedulingApp.forms import *
from classschedulingApp.models import *
class UserAdmin(admin.ModelAdmin):
    
    
    list_display =["username","email","first_name","last_name","is_active","is_staff","student","departmenthead","instructor","is_superuser","address",]
    search_fields=["username","email","first_name","last_name","is_active","is_staff","student","departmenthead","instructor","is_superuser","address",]
    ordering = ["username"]

admin.site.register(User, UserAdmin)
class AttendanceInline(admin.TabularInline):
    model = Attendance
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        AttendanceInline,
    ]
    search_fields=["username","email","first_name","last_name","active","address","student"]
    ordering = ["username"]

    
    list_display =["username","email","first_name","last_name","active","address","student"]

admin.site.register(Student, StudentAdmin)

# class InstructorAdmin(admin.ModelAdmin):

#     #form = InstructorForm
#     search_fields=["uid","name"]
#     ordering = ["name"]

    
#     list_display =["uid","name"]

# admin.site.register(Instructor, InstructorAdmin)

class InstructorsAdmin(admin.ModelAdmin):
    form = InstructorForm
    search_fields=["username","email","first_name","last_name","active","address","instructor","name"]
    ordering = ["username"]

    
    list_display =["username","email","first_name","last_name","active","address","instructor","name"]

admin.site.register(Instructors, InstructorsAdmin)

class DepartmentheadAdmin(admin.ModelAdmin):
    search_fields=["username","email","first_name","last_name","active","address","departmenthead",]
    ordering = ["username"]
    
    list_display =["username","email","first_name","last_name","active","address","departmenthead"]

admin.site.register(Departmenthead, DepartmentheadAdmin)

class  AdministratorAdmin(admin.ModelAdmin):
    search_fields=["username","email","first_name","last_name","active","address","is_superuser"]
    ordering = ["username"]
    list_display =["username","email","first_name","last_name","active","address","is_superuser"]
admin.site.register(Administrator, AdministratorAdmin)     
    
    
 

class AttendanceAdmin(admin.ModelAdmin):
    list_display =["student","morning","attend_at_morning","afternoon","attend_at_afternoon"]
    ordering = ['-date']

admin.site.register(Attendance, AttendanceAdmin)
    









class FeedBackAdmin(admin.ModelAdmin):
   

    list_display =["student","instructor","name","email","subject","message"]
    ordering=['-date']
admin.site.register(FeedBack,FeedBackAdmin)
class NotificationAdmin(admin.ModelAdmin):
   

    list_display =["date","updated"]
    ordering=['-date']


admin.site.register(Notification,NotificationAdmin)





