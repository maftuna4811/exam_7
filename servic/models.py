from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='servic/category/')
    views = models.IntegerField(default=0)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]
        ordering = ['id', 'name']


class Features(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id', 'name']
        indexes = [
            models.Index(fields=['id'])
        ]


class BlogType(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id', 'name']
        indexes = [
            models.Index(fields=['id', 'name'])
        ]


class Blog(models.Model):
    image = models.ImageField(upload_to='servic/blog/')
    name = models.CharField(max_length=60)
    description = models.TextField(null=True)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE, null=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id', 'name']
        indexes = [
            models.Index(fields=['id', 'name'])
        ]


class Services(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    features = models.ForeignKey(Features, on_delete=models.CASCADE)
    image = models.URLField(null=True)
    short_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.short_name

    class Meta:
        ordering = ['id', 'short_name']
        indexes = [
            models.Index(fields=['id', 'short_name'])
        ]
