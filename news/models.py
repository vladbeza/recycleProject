from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Author(models.Model):

    nick_name = models.CharField(max_length=500)

    def __str__(self):
        return str(self.nick_name)


class NewPost(models.Model):

    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='news/%Y/%m/%d/', blank=True)
    short_image = models.ImageField(upload_to='news/%Y/%m/%d/', blank=True, max_length=80)
    pub_date = models.DateTimeField(verbose_name="pub news date", auto_now_add=True)
    short_description = models.CharField(blank=True, max_length=200)
    text = RichTextUploadingField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return str(self.title)

    def get_abs_url(self):
        return reverse("news:post_details", args=[self.id])

class Comment(models.Model):

    post = models.ForeignKey(NewPost, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text