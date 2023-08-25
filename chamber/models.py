from django.db import models

# Create your models here.

class Appeals(models.Model):
    company_name = models.CharField(max_length=150, verbose_name="Korxona yoki tashkilot nomi")
    address = models.CharField(max_length=255, verbose_name="Korxona manzili")
    name = models.CharField(max_length=200, verbose_name="Murojaatchi FIO")
    phone_number = models.CharField(max_length=20, verbose_name="Telefon raqami")
    content_appeal = models.TextField(verbose_name="Murojaat mazmuni", unique=True)
    type_appeal = models.CharField(max_length=30, verbose_name="Murojaat turi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Murojaat qilingan vaqt")

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Murojaat"
        verbose_name_plural = "Murojaatlar"
