from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Kategoriya", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='Maqola nomi')
    content = models.TextField(blank=True, verbose_name='Maqola matni')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'yilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yagilangan vaqti')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Rasmi')
    published = models.BooleanField(default=True, verbose_name="Qo'shish")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriya')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'
        ordering = ['-created_at']
