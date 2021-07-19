from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from . models import feed, meter 
import os
import json
import csv
import datetime

# Create your views here.
def index(request):
	template='posts/index.html'
	results=feed.objects.all()
	jsondata = serializers.serialize('json',results)
	context={
		'results':results,
		'jsondata':jsondata,
	}
	return render(request,template,context)

def getdata(request):
	results=feed.objects.all()
	jsondata = serializers.serialize('json',results)
	return HttpResponse(jsondata)

def base_layout(request):
	template='posts/base.html'
	return render(request,template)

def import_csv(request):
	dir 	= '/Users/share/data/octopus/csv/'
	dirold 	= '/Users/share/data/octopus/old/'
	arr = sorted(os.listdir(dir), reverse=True)
	hours_added = datetime.timedelta(hours = 1)

	for pdf in arr:
		path = dir + pdf
		pathold = dirold + pdf
		print(pdf)
		if   'meter' in pdf:
			with open(path) as f:
				reader = csv.DictReader(f)
				for row in reader:
					if row['interval_start'][19:] == '+01:00':
						interval_start = (datetime.datetime.strptime(row['interval_start'][:19] + 'Z',"%Y-%m-%dT%H:%M:%S%z")) + hours_added
					else :
						interval_start = (datetime.datetime.strptime(row['interval_start'] ,"%Y-%m-%dT%H:%M:%S%z"))
					# print(interval_start, row['interval_start'],row['interval_start'][19:] , datetime.datetime.strptime (row['interval_start'][:19] ,"%Y-%m-%dT%H:%M:%S"))
					meter.objects.filter(time_from=interval_start).update(consumption	= '{:.3f}'.format(float(row['consumption'])))
		elif 'tarif' in pdf:			
			with open(path) as f:
				reader = csv.DictReader(f) # value_inc_vat	valid_from
				for row in reader:					
					_, created = meter.objects.get_or_create(			# 021-07-07T21:30:00Z
						time_from	= datetime.datetime.strptime (row['valid_from'],"%Y-%m-%dT%H:%M:%S%z") ,
						value		= '{:.3f}'.format(float(row['value_inc_vat'])),
						)
					# print(row['valid_from'])
		else :
			print(pdf)
		
		os.rename(path, pathold)

	template='posts/meter.html'
	results=meter.objects.all().order_by('-time_from')
	jsondata = serializers.serialize('json',results)
	context={
		'results':results,
		'jsondata':jsondata,
	}
	return render(request,template,context)

def getmeter(request):
	results=meter.objects.all().order_by('-time_from')
	jsondata = serializers.serialize('json',results)
	return HttpResponse(jsondata)

def meter(request):
	template='posts/meter.html'
	return render(request,template)

def index_posts(request):
	template='posts/posts.html'
	return render(request,template)
