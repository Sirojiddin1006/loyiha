from django.db import models
class Janri(models.Model):
    name = models.CharField(max_length=100,verbose_name='Janri')
    def __str__(self):
        return self.name
    class Meta:

        verbose_name_plural = 'Janri'
class Muallif(models.Model):
    fullname=models.CharField(max_length=100,verbose_name='<FISH')
    def __str__(self):
        return self.fullname
    class Meta:
        verbose_name_plural = 'Mallif'

class Book(models.Model):
    name= models.CharField(max_length=100,verbose_name='<Nomi')
    janri=models.ForeignKey(Janri, on_delete=models.CASCADE)
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)
    sahifalar=models.IntegerField(verbose_name='Sahifalar',default=1)
    class Meta:
        verbose_name_plural = 'Book'
    def __str__(self):
        return self.name








# Create your models here.
