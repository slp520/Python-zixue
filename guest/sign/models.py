from django.db import models

# Create your models here.
#发布会表
class Event(models.Model):
    name=models.CharField(max_length=100) #发布会标题、人数、状态、地址、发布会时间、创建时间
    limit=models.IntegerField()
    status=models.BooleanField()
    address=models.CharField(max_length=200)
    start_time=models.DateTimeField('event_time')
    create_time=models.DateTimeField(auto_now=True)

#__str__()方法告诉 Python 如何将对象以 str 的方式显示出来。 所以， 为每个模型类添加了__str__()方法
    def __str__(self):
        return self.name

#嘉宾表
class Guest(models.Model):
    event=models.ForeignKey(Event) #关联发布会表的ID、姓名、手机号、邮箱、状态、创建时间
    real_name=models.CharField(max_length=64)
    phone=models.CharField(max_length=16)
    mail=models.EmailField()
    sign=models.BooleanField()
    create_time=models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=("event","phone")

    def __str__(self):
        return self.real_name