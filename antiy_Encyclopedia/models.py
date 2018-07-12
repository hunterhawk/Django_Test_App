from django.db import models

# Create your models here.
class Process_Test(models.Model):
    path = models.CharField(u'path', max_length=512)
    company = models.CharField(u'company', max_length=256)
    product = models.CharField(u'product', max_length=256)
    description = models.TextField(u'description')
    create_time = models.DateTimeField(u'create_time', auto_now_add=True, editable=True)
    author = models.CharField(u'author', max_length=256)
    # pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    # update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.path