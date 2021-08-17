from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=200)
    stu_username=models.CharField(max_length=40, default='')
    stu_password=models.CharField(max_length=40, default='')
    student_score= models.IntegerField(default=0) # keeps tally of student score in Quiz session
    def __str__(self):
        return self.student_name

class Question(models.Model):
    question_text = models.CharField(max_length=200) 
    right_choice = models.IntegerField(default = 1) #indicates correct choice for each Ques. object
    q_attempted= models.IntegerField(default=0) # to check if the question is attempted yet in the Quiz or not

    def __str__(self):
        # if(right_choice==0): right_choice=1 # Doing this because for some reason the defualt value isnt getting shifted to 1, 
        #                                     #and it is necessary for this to happen to avoid accessing incorrect QuesrySet index as its index starts from 1
        return self.question_text
    def display_answer(self):
        corr_choice= self.choice_set.get(choice_seq=self.right_choice)
        answer= corr_choice.choice_text
        return (answer)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_seq = models.IntegerField(default=1) # Willl Store at which position i.e. (1-4) will the option be displayed and correspond to for the question
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text