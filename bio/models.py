from django.db import models

class About(models.Model):
    """
    About Section Model for home page
    """

    class Meta:
        verbose_name_plural = "About Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.name


class Assisted(models.Model):
    """
    About Section Model for home page
    """

    class Meta:
        verbose_name_plural = "Assisted Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.name


class Shows(models.Model):
    """
    About Section Model for home page
    """

    class Meta:
        verbose_name_plural = "Shows Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name