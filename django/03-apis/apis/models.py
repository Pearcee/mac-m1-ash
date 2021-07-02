from django.conf import settings
from django.db import models
from django.utils import timezone

# Entry some data into model
class books(models.Model):
    book_name = models.CharField(max_length=10)
    author_name = models.CharField(max_length=10)
    book_price = models.IntegerField()
    book_quantity = models.IntegerField()
 
# Create a string representation
    def __str__(self):
        return self.book_name

# api/models.py
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.title

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)        

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('apis.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)        

class Staff(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class tarif(models.Model):
    value = models.DecimalField( max_digits=3, decimal_places=3) # value_inc_vat
    Timestamp = models.DateTimeField(blank=False, null=True)
 
    def __str__(self):
        return self.Timestamp

class meter(models.Model):
    consumption = models.DecimalField( max_digits=3, decimal_places=3)
    Timestamp = models.DateTimeField(blank=False, null=True)
 
    def __str__(self):
        return self.Timestamp

class online(models.Model):
    Timestamp = models.DateTimeField(blank=False, null=True)
    ip = models.CharField(max_length=62)
    name = models.CharField(max_length=64)
 
    def __str__(self):
        return self.Timestamp

class speedtest(models.Model):
    ServerID = models.IntegerField( )
    Timestamp = models.DateTimeField(blank=False, null=True)
    Distance = models.DecimalField( max_digits=12, decimal_places=8)
    Ping = models.DecimalField( max_digits=3, decimal_places=3)
    Download = models.DecimalField( max_digits=10, decimal_places=2)
    Upload = models.DecimalField( max_digits=10, decimal_places=2)
    ip = models.CharField(max_length=62)

    def __str__(self):
        return self.Timestamp        

"""  
Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload,Share,IP Address
4058	Wildcard Networks	Newcastle upon Tyne	2021-06-23T09:15:13.173107Z	105.4279453	39.982	69624980.03	18494139.82		86.177.254.153
10602	Aspire Technology Solutions	Gateshead	2021-06-23T09:45:09.957434Z	106.1429491	29.023	43132640.01	17716995.05		86.177.254.153
10602	Aspire Technology Solutions	Gateshead	2021-06-23T10:15:12.453044Z	106.1429491	28.932	70095792.76	18465945.29		86.177.254.153
4058	Wildcard Networks	Newcastle upon Tyne	2021-06-23T10:45:13.237917Z	105.4279453	30.772	69977558.18	18583131.91		86.177.254.153


01/06/2021 00:00	 192.168.1.110	 p110


tarif
value_exc_vat,value_inc_vat,valid_from,valid_to
15.96,16.758,2021-06-25T21:30:00Z,2021-06-25T22:00:00Z

meter

consumption,interval_start,interval_end
0.073,2021-06-24T00:00:00+01:00,2021-06-24T00:30:00+01:00
"""