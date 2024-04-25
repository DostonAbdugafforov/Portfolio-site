from django.db import models
from django.utils import timezone


class BlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class BlogCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Blog(models.Model):
    OPTIONS = (
        ('draft', "Qoralama"),
        ('published', "Nashir etilgan")
    )
    title = models.CharField(max_length=350, verbose_name="Sarlavha")
    category = models.ForeignKey('BlogCategory', on_delete=models.PROTECT, default=1, related_name='categories')
    photo = models.ImageField(upload_to="blog", default="/blog/ccM9pdX9DDiNs05Bu5BhVAr7S2GbOafc.jpg")
    short_content = models.TextField(verbose_name="Qisqa ma`lumot")
    content = models.TextField(verbose_name="Ma`lumot")
    pub_date = models.DateTimeField(default=timezone.now(), verbose_name="Nashir Sanasi")
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=250, choices=OPTIONS, default="draft", verbose_name="Holati")
    objects = models.Manager()
    manager = BlogManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]





class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta:
        ordering = ('publish', )


    def __str__(self):
        return self.name





class AboutMe(models.Model):
    short_content = models.CharField(max_length=255, verbose_name="Qisqa ma'lumot")
    content = models.TextField(verbose_name="To'liq ma'lumot")
    photo = models.ImageField(upload_to='about_me/', verbose_name='Rasm')

    def __str__(self):
        return self.short_content





class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.TextField()


    def __str__(self):
        return self.name



