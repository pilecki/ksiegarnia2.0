from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    genre = models.ForeignKey('Genre', null=True,
                              blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promotion = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateField(auto_now_add=True)
    author1 = models.ForeignKey('Authors', null=True,
                                blank=True, on_delete=models.SET_NULL,
                                related_name='author1')
    author2 = models.ForeignKey('Authors', null=True,
                                blank=True, on_delete=models.SET_NULL,
                                related_name='author2')
    formats = models.ForeignKey('Formats', null=True,
                                blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ComingSoon(models.Model):

    class Meta:
        verbose_name_plural = 'Comming Soon'

    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    available_date = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Formats(models.Model):

    class Meta:
        verbose_name_plural = 'Formats'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Authors(models.Model):

    class Meta:
        verbose_name_plural = 'Authors'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
