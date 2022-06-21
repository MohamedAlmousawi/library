from django.db import models

# Create your models here.

class State(models.Model):
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.status
class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category


class Book(models.Model):

    title = models.CharField('اسم الكتاب: ',max_length=50)
    auther= models.CharField('اسم المؤلف: ',max_length=50,null=True,blank=True)
    book_image = models.ImageField("صورة الكتاب",upload_to ='images/books',null=True,blank=True)
    auther_image = models.ImageField("صورة الكتاب",upload_to ='images/authers',null=True,blank=True)
    pages = models.IntegerField('عدد الصفحات : ',default=1,null=True,blank=True)
    status = models.ForeignKey(State,on_delete=models.CASCADE)
    prise =models.DecimalField('السعر : ',max_digits=5,decimal_places=2,null=True,blank=True)
    rented_prise_day =models.DecimalField('سعر التأجير في اليوم: ',max_digits=5,decimal_places=2,null=True,blank=True)
    rented_time = models.IntegerField('مدة التأجير : ',null=True,blank=True)
    rented_prise = models.DecimalField('سعر التأجير النهائي : ',max_digits=5,decimal_places=2,null=True,blank=True)
    book_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


