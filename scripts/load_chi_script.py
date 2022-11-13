from pickups.models import Park
import csv
import pandas

def run():
    df = pandas.read_csv('park_data/CPD_Parks.csv')
    Park.objects.all().delete()
    for i in df.index:
        if pandas.isnull(df['ZIP'][i]):
            code = 'nan'
        else:
            code = df['ZIP'][i]
        park = Park(name = df['LABEL'][i],
                    address = df['LOCATION'][i],
                    city = 'Chicago',
                    state = 'Illinois',
                    zipcode = code,
                    basketball = bool(df['BASKETBALL'][i] > 0),
                    football = bool(df['FOOTBALL_S'][i] > 0),
                    baseball = bool(df['BASEBALL_J'][i] > 0),
                    volleyball = bool(df['VOLLEYBALL'][i] > 0),
                    tennis = bool(df['TENNIS_COU'][i] > 0),
                    handball = bool(df['HANDBALL_R'][i] > 0),
                    cricket = bool(df['CRICKET_FI'][i] > 0))

        park.save()
