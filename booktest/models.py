from django.db import models

# Create your models here.


class BookInfo(models.Model):

    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):

    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    hbook = models.ForeignKey('BookInfo', on_delete=models.DO_NOTHING)
    isDelete = models.BooleanField(default=False)


class NewsType(models.Model):

    type_name = models.CharField(max_length=20)


class NewsInfo(models.Model):

    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    news_type = models.ManyToManyField('NewsType')


class EmployeeBasicInfo(models.Model):

    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)
    age = models.IntegerField()


class EmployeeDetailInfo(models.Model):

    addr = models.CharField(max_length=256)
    employee_basic = models.OneToOneField('EmployeeBasicInfo', on_delete=models.DO_NOTHING)


class AreaInfo(models.Model):

    aTitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)


