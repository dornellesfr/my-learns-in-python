from datetime import datetime

fmt = '%d/%m/%Y'
# date = datetime(2000, 12, 18, 7, 59, 23)

date = datetime.strptime('2000-12-18 07:59:23', '%Y-%m-%d %H:%M:%S')

print(date.strftime(fmt))
