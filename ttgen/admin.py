from django.contrib import admin
from ttgen.models import *
from .forms import *
class RoomAdmin(admin.ModelAdmin):
    
    list_display =['r_number','seating_capacity']
admin.site.register(Room,RoomAdmin)
class MeetingTimeAdmin(admin.ModelAdmin):
    
    list_display =['pid','time','day',]
admin.site.register(MeetingTime,MeetingTimeAdmin)
class CourseAdmin(admin.ModelAdmin):
    
    list_display =['course_number','course_name','max_numb_students','get_instructors',]
admin.site.register(Course,CourseAdmin)
class DepartmentAdmin(admin.ModelAdmin):
    
    list_display =['dept_name','get_course']
admin.site.register(Department,DepartmentAdmin)
class SectionAdmin(admin.ModelAdmin):
    
    list_display =['section_id','department','num_class_in_week','course','meeting_time','room','instructor']
admin.site.register(Section,SectionAdmin)

class InstructorAdmin(admin.ModelAdmin):

    form = InstructorAddForm
    search_fields=["uid","name"]
    ordering = ["name"]

    
    list_display =["uid","name"]

admin.site.register(Instructor, InstructorAdmin)