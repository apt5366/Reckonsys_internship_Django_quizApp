from django.contrib import admin

from .models import Question, Choice, Student

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Correct Answer',      {'fields': ['right_choice']}), 
        ('Question Attempted By Student Yet (0-No, 1- Yes)', {'fields': ['q_attempted'], 'classes':
        ['collapse']})
        ]

    inlines= [ChoiceInline]

    list_display = ('question_text','right_choice', 'q_attempted')

admin.site.register(Question, QuestionAdmin)


# admin.site.register(Choice)
admin.site.register(Student)