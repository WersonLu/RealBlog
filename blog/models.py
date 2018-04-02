# -*-coding:utf8-*-
from django.db import models
# from django.urls import reverse
# Create your models here.
import markdown
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.utils.six import python_2_unicode_compatible


# 分类
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"分类")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"标签")

    def __str__(self):
        return self.name


# 文章
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70, verbose_name=u"标题")
    body = models.TextField(verbose_name=u"正文")

    created_time = models.DateTimeField(verbose_name=u"创建时间")
    modified_time = models.DateTimeField(verbose_name=u"修改时间")

    excerpt = models.CharField(max_length=200, blank=True, verbose_name=u"摘要")

    category = models.ForeignKey(Category, verbose_name=u"分类")
    tags = models.ManyToManyField(Tag, verbose_name=u"标签")

    author = models.ForeignKey(User, verbose_name=u"作者")
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = u"文章信息"
        verbose_name_plural = verbose_name
        # ordering=['-created_time'] 可以指定排序规则

    def __str__(self):
        return self.title

    # 博客文章的绝对路径
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase(self):
        self.views += 1
        self.save(update_fields=['views'])

    # {{ post.body | truncatechars:54 }}  摘要方法一  模板标签过滤器
    # 摘要方法二
    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 20个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:20]
        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)


# 留言板
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"用户名")
    email = models.EmailField(max_length=255, verbose_name=u"邮箱")
    # url = models.URLField(blank=True)
    # 主题
    subject = models.CharField(max_length=200, verbose_name=u"主题")
    text = models.TextField(verbose_name=u'正文')
    # slug=models.SlugField(max_length=100,unique_for_date='created_time')
    created_time = models.DateTimeField(auto_now_add=True)

    # post = models.ForeignKey('blog.Post')
    class Meta:
        verbose_name = u'留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20]

    def get_absolute_url(self):
        return reverse('blog:msg', kwargs={'pk': self.pk})


# 评论系统,本想用一个type来做,但是我的留言板又不对应文章
@python_2_unicode_compatible
class CommentPost(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = u'文章评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
