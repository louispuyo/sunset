from django.db import models
# Create your models here.

# Create your models here.

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class materials(models.Model):
    name = models.CharField(null=True, max_length=50)
    origin = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.name


class Bracelet(models.Model):
    name = models.CharField(max_length=50)


class collection(models.Model):
    name = models.CharField(max_length=50)
    #date = models.DateTimeField()
    #available = models.BooleanField(default=False)


class watch(models.Model):
    name = models.CharField(max_length=50)
    #collection = models.OneToOneField(collection, on_delete=models.CASCADE)
    description = models.TextField()
    discount_price = models.FloatField(blank=True, null=True)
    image = models.ImageField()
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("watch:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("watch:add-to-cart", kwargs={
            'slug': self.slug
        })


class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    cart = models.IntegerField()
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)


class order(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    #! settings.AUTH...
    #!


class orderWatch(models.Model):
    pass


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code

# settings.AUTH_USER_MODEL for -> user status
