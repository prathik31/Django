# user----prathik           pass----123ewqasd


from django.db import models
import pandas as pd
# Create your models here.


class profile(models.Model):
    username=models.CharField(max_length=50)
    fullname=models.CharField(max_length=50,blank=True)
    email=models.EmailField(max_length=254)
    bio=models.CharField(max_length=250)
    profile_img=models.ImageField(upload_to='profile_image',default='user.png', blank=True, null=True)
    location=models.CharField(max_length=50, blank=True, null=True)
    GENDER=(
        ('male','male'),
        ('female','female'),
    )
    gender=models.CharField(max_length=6, choices=GENDER, blank=True, null=True)


    def __str__(self):
        return self.username
    
class categories(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class quiz(models.Model):
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    category=models.ForeignKey("categories", on_delete=models.CASCADE)
    quiz_file=models.FileField(upload_to=None, max_length=1000, blank=True, null=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    #to save quiz
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        if self.quiz_file:
            self.import_from_excel()

    
    def import_from_excel(self):
        #to extract questions
        df=pd.read_excel(self.quiz_file.path)

        #iterate over each row
        for index, row in df.iterrows():
            #extract questions,choices,correct answer from excel
            questions_text=row['questions']
            choice_1=row['A']
            choice_2=row['B']
            choice_3=row['C']
            choice_4=row['D']
            correct_answer=row['CORRECT']

            #create quiz object
            Q=questions.objects.get_or_create(quizs=self, text=questions_text)

            #create choice object
            choice2=choices.objects.get_or_create(quest=Q[0], text=choice_2, is_correct=correct_answer=='B')
            choice1=choices.objects.get_or_create(quest=Q[0], text=choice_1, is_correct=correct_answer=='A')
            choice3=choices.objects.get_or_create(quest=Q[0], text=choice_3, is_correct=correct_answer=='C')
            choice4=choices.objects.get_or_create(quest=Q[0], text=choice_4, is_correct=correct_answer=='D')

class questions(models.Model):
    quizs=models.ForeignKey("quiz", on_delete=models.CASCADE)
    text=models.CharField(max_length=510)

    def __str__(self):
        return self.text[:50]
    

class choices(models.Model):
    quest=models.ForeignKey("questions", on_delete=models.CASCADE)
    text=models.CharField( max_length=510)
    is_correct=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.quest.text[:20]
    
