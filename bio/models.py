from django.db import models

class About(models.Model):
    """
    About Section Model for home page
    """

    class Meta:
        verbose_name_plural = "About Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Assisted(models.Model):
    """
    Assisted Section Model for home page
    """

    class Meta:
        verbose_name_plural = "Assisted Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Shows(models.Model):
    """
    Shows Section Model for home page
    """

    class Meta:
        verbose_name_plural = "Shows Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Editorials(models.Model):
    """
    Editorials Section Model for home page
    """

    class Meta:
        verbose_name_plural = "Editorials Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Celebrities(models.Model):
    """
    Celebrities Section Model for home page
    """

    class Meta:
        verbose_name_plural = "Celebrities Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Music(models.Model):
    """
    Music Section Model for home page
    """

    class Meta:
        verbose_name_plural = "Music Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Tv(models.Model):
    """
    TV Section Model for home page
    """

    class Meta:
        verbose_name_plural = "TV Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Commercials(models.Model):
    """
    Commercials Section Model for home page
    """

    class Meta:
        verbose_name_plural = "Commercials Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name