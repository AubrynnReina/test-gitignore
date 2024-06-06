
import airflow
import awscli
import bs4
import requests
import selenium
import sys

import findspark
findspark.init()
import pyspark

print('Python version:', sys.version.split(' ')[0])
print('Airflow version:', airflow.__version__)
print('Selenium version:', selenium.__version__)
print('Requests version:', requests.__version__)
print('BeautifulSoup version:', bs4.__version__)
print('AWS CLI version:', awscli.__version__)
print('PySpark version:', pyspark.__version__)
