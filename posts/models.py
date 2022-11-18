from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    
    def __str__(self):
        return str(self.user)
    
    
class SelectedFood(models.Model):
    BREAKFAST = (
        ('IDLI-SAMBAR', 'Idli-Sambar'),
        ('PUTTU-KADALA', 'Puttu-Kadala'),
        ('APPAM-STEW', 'Appam-Stew'),
    )
    LUNCH = (
        ('BIRIYANI', 'Biriyani'),
        ('RICE-CURRY', 'Rice-curry'),
        ('KANJI', 'Kanjis'),
    )
    SNACKS = (
        ('TEA', 'Tea'),
        ('COFFE', 'Coffe'),
        ('PUFFS', 'Puffs'),
    )
    SUPPER = (
        ('CHAPPATHI-CHICKEN', 'Chappathi-Chicken'),
        ('POORI-CURRY', 'Poori-Curry'),
        ('MASALA-DOSA', 'Masala Dosa'),
    )
    
    breakfast1 = models.CharField(choices=BREAKFAST,max_length=64)
    lunch1 = models.CharField(choices=LUNCH, max_length=64)
    snacks1 = models.CharField(choices=SNACKS, max_length=64)
    supper1 = models.CharField(choices=SUPPER, max_length=64)
    date1 = models.DateField()
    breakfast2 = models.CharField(choices=BREAKFAST,max_length=64)
    lunch2 = models.CharField(choices=LUNCH, max_length=64)
    snacks2 = models.CharField(choices=SNACKS, max_length=64)
    supper2 = models.CharField(choices=SUPPER, max_length=64)
    date2 = models.DateField()
    breakfast3 = models.CharField(choices=BREAKFAST,max_length=64)
    lunch3 = models.CharField(choices=LUNCH, max_length=64)
    snacks3 = models.CharField(choices=SNACKS, max_length=64)
    supper3 = models.CharField(choices=SUPPER, max_length=64)
    date3 = models.DateField()
    breakfast4 = models.CharField(choices=BREAKFAST,max_length=64)
    lunch4 = models.CharField(choices=LUNCH, max_length=64)
    snacks4 = models.CharField(choices=SNACKS, max_length=64)
    supper4 = models.CharField(choices=SUPPER, max_length=64)
    date4 = models.DateField()
    breakfast5 = models.CharField(choices=BREAKFAST,max_length=64)
    lunch5 = models.CharField(choices=LUNCH, max_length=64)
    snacks5 = models.CharField(choices=SNACKS, max_length=64)
    supper5 = models.CharField(choices=SUPPER, max_length=64)
    date5 = models.DateField()
    breakfast6 = models.CharField(choices=BREAKFAST,max_length=64)
    lunch6 = models.CharField(choices=LUNCH, max_length=64)
    snacks6 = models.CharField(choices=SNACKS, max_length=64)
    supper6 = models.CharField(choices=SUPPER, max_length=64)
    date6 = models.DateField()
    breakfast7 = models.CharField(choices=BREAKFAST,max_length=64)
    lunch7 = models.CharField(choices=LUNCH, max_length=64)
    snacks7 = models.CharField(choices=SNACKS, max_length=64)
    supper7 = models.CharField(choices=SUPPER, max_length=64)
    date7 = models.DateField()
    
    student = models.ForeignKey('posts.Students', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Selected Food"
        verbose_name_plural = "Selected Food"
        
    def __str__(self):
        return str(self.student)
