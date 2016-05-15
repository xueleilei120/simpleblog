# coding=utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    class Meta:
        app_label = 'blog'
        verbose_name = '��ǩ'
        verbose_name_plural = '��ǩ'

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        app_label = 'blog'
        verbose_name = '����Ŀ¼'
        verbose_name_plural = '����Ŀ¼'

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        app_label = 'blog'
        verbose_name = '����'
        verbose_name_plural = '����'

    # ����
    author = models.ForeignKey(User)
    # ����
    title = models.CharField(max_length=200)
    # ����
    text = models.TextField()
    # ��ǩ
    tags = models.ManyToManyField(Tag)
    # ����Ŀ¼
    category = models.ForeignKey(Category)
    # �����
    click = models.IntegerField(default=0)
    # ����ʱ��
    created_date = models.DateTimeField(default=timezone.now)
    # ����ʱ��
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        app_label = 'blog'
        verbose_name = '����'
        verbose_name_plural = '����'

    author = models.CharField(max_length=20)
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post)

    def __str__(self):
        return '{0}: {1}'.format(self.author, self.post.title)


class Evaluate(models.Model):
    class Meta:
        app_label = 'blog'
        verbose_name = '����'
        verbose_name_plural = '����'

    ip = models.CharField(max_length=40)
    evaluate = models.IntegerField()
    post = models.ForeignKey(Post)

    def __str__(self):
        return '{0}: {1}'.format(self.ip, self.evaluate)


class Page(models.Model):
    class Meta:
        app_label = 'blog'
        verbose_name = 'ҳ��'
        verbose_name_plural = 'ҳ��'

    # ����
    author = models.ForeignKey(User)
    # ����
    title = models.CharField(max_length=200)
    # ����
    text = models.TextField()
    # ����˳��
    porder = models.IntegerField(default=0)
    # ����ʱ��
    created_date = models.DateTimeField(default=timezone.now)
    # ����ʱ��
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title