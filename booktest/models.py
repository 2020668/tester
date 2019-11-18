from django.db import models

# Create your models here.


class BookInfoManage(models.Manager):
    """图书模型管理器类"""
    # 改变查询的结果集
    def all(self):
        book = super().all()
        books = book.filter(isDelete=False)
        return books

    def create_book(self, btitle, bpub_date):
        # 创建一个图书对象
        model_class = self.model
        book = model_class()
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book


class BookInfo(models.Model):

    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    # book = models.Manager()
    objects = BookInfoManage()

    class Meta:
        db_table = 'bookinfo'       # 指定模型类对应的表名


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

    areaName = models.CharField(max_length=20)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)
    shortName = models.CharField(max_length=50)
    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)
    level = models.IntegerField()
    position = models.CharField(max_length=255)
    sort = models.IntegerField()
