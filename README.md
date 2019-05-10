# blog

简单轻便的个人博客

使用Django开发,有什么技术文章可以直接在Django的管理界面编辑

部署只需执行初始化操作即可,迁移博客只需直接移动整个文件夹即可

**支持`markdown`语法,插入图片需要手动将图片放到**

```blog\artical\static\artical\temp.jpg```

**编辑文章中用`markdown`语法引用图片**

```
![temp](/static/artical/temp.jpg)
```

![样式图1](https://raw.githubusercontent.com/gwjczwy/blog/master/layout.png)

![样式图2](https://raw.githubusercontent.com/gwjczwy/blog/master/artical_screen.png)

# 初始化

```
pip install markdown
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py createsuperuser
 ```
