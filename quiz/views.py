from django.http import HttpResponse,  HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.urls import reverse

from .models import Choice, Question, Student

def index(request):
    # question_list = Question.objects.all()
    # context = {'question_list': question_list}
    return render(request, 'quiz/index.html')

def login_request(request): #

    # question = get_object_or_404(Question, pk=question_id)

    valid=0 # indicates whether login was success or failure 
    username=request.POST.get('username')
    password=request.POST.get('password')

    try:
        student = Student.objects.get(stu_username=username)
        # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Student.DoesNotExist):
        # Redisplay the question form.
        return render(request, 'quiz/index.html', {
            'error_message': "Incorrect Username entered. Please try again.",
        })
    else:

        if(student.stu_password != password):
            return render(request, 'quiz/index.html', {
            'error_message': "Incorrect password entered. Please try again.",
        })
        else: 
            student.student_score=0 # Sets student score counter to 0 for a fresh start to the Quiz
            student.save()

            # Setting all questions attempted to 0 at the starting of a new quiz session
            question_list = Question.objects.all()

            for q in question_list:
                q.q_attempted = 0 #indicates that questions has not been attempted once as this is start of new Quiz session 
                q.save() 
                

            return HttpResponseRedirect(reverse('quiz:questions', args=(student.id,)))




def questions(request, student_id):

    question_list = Question.objects.all()
    # context = {'question_list': question_list}
    student= get_object_or_404(Student, pk=student_id)

    print('<<<<<< ....Student ID is %s  ' % student_id)
    context = {'question_list': question_list, 'student' : student}
    return render(request, 'quiz/questions.html', context)


def detail(request, question_id, student_id):
    student= get_object_or_404(Student, pk=student_id)
    try:

        question = Question.objects.get(pk=question_id)
        
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'quiz/detail.html', {'question': question ,'student' : student })

def checkAns(request, question_id, student_id): #checks whether the answer attempted is correct or not, and increments StudnetScore accordingly

    question = get_object_or_404(Question, pk=question_id)
    student=get_object_or_404(Student,pk=student_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question form.
        return render(request, 'quiz/detail.html', {
            'question': question,
            'student' : student,
            'error_message': "You didn't select a choice.",
        })
    else:
        

        #answer indicates whether attempt was correct or not 
        answer = 1 if (selected_choice.choice_seq==question.right_choice) else 0 

        if(answer==1): # answer correct
            if(question.q_attempted==0): # 0 -- Qn was not previosuly attempted
                student.student_score =student.student_score + 10 #Student gets 10 points
                student.save()
            else: # Qn was attempted previously
                if(question.q_attempted!=question.right_choice): # Qn was attempted incorrectly previously
                    student.student_score =student.student_score+10 #Student gains 10 points as he/she has modified their answer and got it right this time
                    student.save()
                
                # No else as Qn was attempted correctly last time as well, so we dont make any change
        else: # Answer wrong in this attempt
            if(question.q_attempted==question.right_choice): # Qn WAS previously attempted correctly
                student.student_score =student.student_score-10 #Student looses 10 points as he/she has modified their answer
                student.save()
            # No else cauz it was not prev attempted and it isnt correct now, so No change in score
        
        question.q_attempted = selected_choice.choice_seq #indicates that questions has been attempted once so score should be incr or decr accordingly
        question.save()





        # if(answer==1): # answer correct
        #     if(question.q_attempted==0): # Qn was not previosuly attempted
        #         student.student_score =student.student_score + 10 #Student gets 10 points
        #         student.save()
        #     #No else cauz it was prev attempted and it was correct so No change in score
        # else: # Answer wrong in this attempt
        #     if(question.q_attempted==1): # Qn WAS previously attempted
        #         student.student_score =student.student_score-10 #Student looses 10 points as he/she has modified their answer
        #         student.save()
        #     # No else cauz it was not prev attempted and it isnt correct now, so No change in score
        
        # question.q_attempted = 1 #indicates that questions has been attempted once so score should be incr or decr accordingly
        # question.save()

        return HttpResponseRedirect(reverse('quiz:questions', args=(student.id,)))
        # return HttpResponseRedirect(reverse('quiz:index', args=(question.id,)))

def submit(request, student_id):

    # question = get_object_or_404(Question, pk=question_id)

    student=get_object_or_404(Student,pk=student_id)
    question_list = Question.objects.all()
    context = {'question_list': question_list, 'student' : student}
    return render(request, 'quiz/submit.html', context)


    

