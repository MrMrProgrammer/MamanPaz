from django.db import models
from BaseApp.models import User
from Food.models import FoodsModel
from jdatetime import datetime as jdatetime


class UserExperience(models.Model):
    icon = models.ImageField(upload_to='UserExperience')
    text = models.CharField(max_length=10)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'UX'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodsModel, on_delete=models.CASCADE)
    UX = models.ForeignKey(UserExperience, on_delete=models.CASCADE)
    text = models.TextField()
    is_answered = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def persian_date(self):
        jdate = jdatetime.fromgregorian(datetime=self.date)
        return jdate.strftime("%Y/%m/%d %H:%M")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        db_table = 'Comment'


class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text

    class Meta:
        db_table = 'Answer'
