

from django.utils import timezone
from django.db import models
import datetime

# Create your models here.

#  需要 Question 和 Choice 两个模型
#  两个模型下面要有对应的字段，每个字段都是 Field 类的实例

# models修改之后需要对数据库进行迁移（migrate）
#   编辑 models.py 文件，改变模型。
#   运行 python manage.py makemigrations 为模型的改变生成迁移文件。
#   运行 python manage.py migrate 来应用数据库迁移。


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >=timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
