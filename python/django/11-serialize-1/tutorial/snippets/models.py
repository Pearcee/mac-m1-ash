from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
NAME_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']


class Users(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name                 = models.CharField(choices=NAME_CHOICES, max_length=100, blank=True, default='')
    username             = models.CharField(max_length=100, blank=True, default='')
    email                = models.CharField(max_length=100, blank=True, default='')
    address_street       = models.CharField(max_length=100, blank=True, default='')
    address_suite        = models.CharField(max_length=100, blank=True, default='')
    address_city         = models.CharField(max_length=100, blank=True, default='')
    address_zipcode      = models.CharField(max_length=100, blank=True, default='')
    address_geo_lat      = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    address_geo_lng      = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    phone                = models.CharField(max_length=100, blank=True, default='')
    website              = models.CharField(max_length=100, blank=True, default='')
    company_name         = models.CharField(max_length=100, blank=True, default='')
    company_catchphrase  = models.CharField(max_length=100, blank=True, default='')
    company_bs           = models.CharField(max_length=100, blank=True, default='')
    picture              = models.URLField(max_length=100, blank=True, default='https://randomuser.me/api/portraits/men/33.jpg')
    class Meta:
        ordering = ['created']


# CREATE TABLE mytable(
#    id                  INTEGER 
#   ,name                VARCHAR(30)
#   ,username            VARCHAR(30)
#   ,email               VARCHAR(30)
#   ,address/street      VARCHAR(30)
#   ,address/suite       VARCHAR(30)
#   ,address/city        VARCHAR(30)
#   ,address/zipcode     VARCHAR(30)
#   ,address/geo/lat     NUMERIC(30,4)
#   ,address/geo/lng     NUMERIC(30,4)
#   ,phone               VARCHAR(30)
#   ,website             VARCHAR(30)
#   ,company/name        VARCHAR(30)
#   ,company/catchphrase VARCHAR(30)
#   ,company/bs          VARCHAR(30)
# );   
# 
#      
'''  
INSERT INTO snippets_users(created,id,name,username,email,address_street,address_suite,address_city,address_zipcode,address_geo_lat,address_geo_lng,phone,website,company_name,company_catchphrase,company_bs) VALUES ('2008-11-11',1,'Leanne Graham','Bret','Sincere@april.biz','Kulas Light','Apt. 556','Gwenborough','92998-3874',-37.3159,81.1496,'1-770-736-8031 x56442','hildegard.org','Romaguera-Crona','Multi-layered client-server neural-net','harness real-time e-markets');
INSERT INTO snippets_users(created,id,name,username,email,address_street,address_suite,address_city,address_zipcode,address_geo_lat,address_geo_lng,phone,website,company_name,company_catchphrase,company_bs) VALUES ('2008-11-11',2,'Ervin Howell','Antonette','Shanna@melissa.tv','Victor Plains','Suite 879','Wisokyburgh','90566-7771',-43.9509,-34.4618,'010-692-6593 x09125','anastasia.net','Deckow-Crist','Proactive didactic contingency','synergize scalable supply-chains');
INSERT INTO snippets_users(created,id,name,username,email,address_street,address_suite,address_city,address_zipcode,address_geo_lat,address_geo_lng,phone,website,company_name,company_catchphrase,company_bs) VALUES ('2008-11-11',3,'Clementine Bauch','Samantha','Nathan@yesenia.net','Douglas Extension','Suite 847','McKenziehaven','59590-4157',-68.6102,-47.0653,'1-463-123-4447','ramiro.info','Romaguera-Jacobson','Face to face bifurcated interface','e-enable strategic applications');
INSERT INTO snippets_users(created,id,name,username,email,address_street,address_suite,address_city,address_zipcode,address_geo_lat,address_geo_lng,phone,website,company_name,company_catchphrase,company_bs) VALUES ('2008-11-11',4,'Patricia Lebsack','Karianne','Julianne.OConner@kory.org','Hoeger Mall','Apt. 692','South Elvis','53919-4257',29.4572,-164.2990,'493-170-9623 x156','kale.biz','Robel-Corkery','Multi-tiered zero tolerance productivity','transition cutting-edge web services');
INSERT INTO snippets_users(created,id,name,username,email,address_street,address_suite,address_city,address_zipcode,address_geo_lat,address_geo_lng,phone,website,company_name,company_catchphrase,company_bs) VALUES ('2008-11-11',5,'Chelsey Dietrich','Kamren','Lucio_Hettinger@annie.ca','Skiles Walks','Suite 351','Roscoeview','33263',-31.8129,62.5342,'(254)954-1289','demarco.info','Keebler LLC','User-centric fault-tolerant solution','revolutionize end-to-end systems');
INSERT INTO snippets_users(created,id,name,username,email,address_street,address_suite,address_city,address_zipcode,address_geo_lat,address_geo_lng,phone,website,company_name,company_catchphrase,company_bs) VALUES ('2008-11-11',6,'Mrs. Dennis Schulist','Leopoldo_Corkery','Karley_Dach@jasper.info','Norberto Crossing','Apt. 950','South Christy','23505-1337',-71.4197,71.7478,'1-477-935-8478 x6430','ola.org','Considine-Lockman','Synchronised bottom-line interface','e-enable innovative applications');
INSERT INTO snippets_users(created,id,name,username,email,address_street,address_suite,address_city,address_zipcode,address_geo_lat,address_geo_lng,phone,website,company_name,company_catchphrase,company_bs) VALUES ('2008-11-11',7,'Kurtis Weissnat','Elwyn.Skiles','Telly.Hoeger@billy.biz','Rex Trail','Suite 280','Howemouth','58804-1099',24.8918,21.8984,'210.067.6132','elvis.io','Johns Group','Configurable multimedia task-force','generate enterprise e-tailers');
INSERT INTO snippets_users(created,id,name,username,email,address_street,address_suite,address_city,address_zipcode,address_geo_lat,address_geo_lng,phone,website,company_name,company_catchphrase,company_bs) VALUES ('2008-11-11',8,'Nicholas Runolfsdottir V','Maxime_Nienow','Sherwood@rosamond.me','Ellsworth Summit','Suite 729','Aliyaview','45169',-14.3990,-120.7677,'586.493.6943 x140','jacynthe.com','Abernathy Group','Implemented secondary concept','e-enable extensible e-tailers');
INSERT INTO snippets_users(created,id,name,username,email,address_street,address_suite,address_city,address_zipcode,address_geo_lat,address_geo_lng,phone,website,company_name,company_catchphrase,company_bs) VALUES ('2008-11-11',9,'Glenna Reichert','Delphine','Chaim_McDermott@dana.io','Dayna Park','Suite 449','Bartholomebury','76495-3109',24.6463,-168.8889,'(775)976-6794 x41206','conrad.com','Yost and Sons','Switchable contextually-based project','aggregate real-time technologies');
INSERT INTO snippets_users(created,id,name,username,email,address_street,address_suite,address_city,address_zipcode,address_geo_lat,address_geo_lng,phone,website,company_name,company_catchphrase,company_bs) VALUES ('2008-11-11',10,'Clementina DuBuque','Moriah.Stanton','Rey.Padberg@karina.biz','Kattie Turnpike','Suite 198','Lebsackbury','31428-2261',-38.2386,57.2232,'024-648-3804','ambrose.net','Hoeger LLC','Centralized empowering task-force','target end-to-end models');
"picture"U
'''