from django.db import models
#处理关于时间的相关事务
from django.utils import timezone
#导入内建的User模型
from django.contrib.auth.models import User

class Artical(models.Model):
    #正文     保存大量文本使用TextField
    body=models.TextField()
    
    #作者   ForeignKey 外键
    author=models.ForeignKey(User,
                             on_delete=models.CASCADE)
    #on_delete 指定删除方式,避免两个关联表的数据不一致


    #创建时间    创建时默认写入现在时间
    created=models.DateTimeField(default=timezone.now)
    #标题 默认使用创建时间的时间戳 同时也作为文章的标识 
    title=models.CharField(max_length=250,blank=True,null=True,default=timezone.now)


    #更新时间     auto_now=True   每次更新数据时自动写入当前时间
    updated=models.DateTimeField(auto_now=True)
    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title

    #查询文章
    def GetArtical(title=''):
        try:
            s=Artical.objects.get(title=title)
            return s
        except 'DoesNotExist':
            return False
            

    

