from models import feed, meter 
import pandas as pd

def import_csv():
	df = pd.read_csv('data/tarif.csv', sep='delimiter')
	meters = []
	for i in range(len(df)):
		meters.append(
			meter(
			date_from	= df.iloc[i][2],
			# consumption = df.iloc[i][1],
			value		= df.iloc[i][1]
			)
		)
	meter.objects.bulk_create(meters)