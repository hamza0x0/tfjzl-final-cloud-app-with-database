from django.contrib import admin
# Import the seven model classes
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# ChoiceInline: edit the choices directly inside a question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# QuestionInline: edit the questions directly inside a course
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# CourseAdmin
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# QuestionAdmin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content', 'course', 'grade']


# LessonAdmin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
