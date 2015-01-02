# by Talha Oz
# @tozCSS

import pandas as pd
from countrycode import countrycode

#Extracted the table using Tabula from Rehman, Scheherazade S., and Hossein Askari.
# “How Islamic Are Islamic Countries?” Global Economy Journal 10, no. 2 (May 21, 2010)
# http://www.degruyter.com/abstract/j/gej.2010.10.2/gej.2010.10.2.1614/gej.2010.10.2.1614.xml
islam = pd.read_csv('Islamicity.csv')
ccodes = countrycode(codes=[ct.strip() for ct in islam.Country.tolist()], origin='country_name', target='iso2c')
# saved it as CSV and uploaded to Google Fusion Tables

# Scraped list from http://en.wikipedia.org/wiki/Member_states_of_the_Organisation_of_Islamic_Cooperation using kimono
results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/bdhe04wo?apikey=VPXUp7hOkUYDIL3wC8GVMHFQcOW3O7HC"))
r = results.get('results').get('collection1')
oic = [ct[u'oic_countries'][u'text'] for ct in r]
oic_codes = countrycode(codes=oic, origin='country_name', target='iso2c')
# saved it as CSV and uploaded this to Google Fusion Tables as well