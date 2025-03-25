from django.db import models
# chop etish
# qoralama
qoralama='QORALAMA'
chop_etish='Chop Etish'
talov =(
    (qoralama, 'QORALAMA'),
    (chop_etish, 'CHOP ETISH'),
)
class Kategoriya(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Kategoriya'

class news(models.Model):
    title = models.CharField(max_length=100)
    kategoriya = models.ForeignKey(Kategoriya, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    slug = models.SlugField(max_length=100)
    xolati= models.CharField(max_length=100, choices=talov, default=qoralama)
    img = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField( auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Xabarlar'