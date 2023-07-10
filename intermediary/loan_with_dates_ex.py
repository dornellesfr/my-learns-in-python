from datetime import datetime
from dateutil.relativedelta import relativedelta
from math import floor

fmt = '%Y-%m-%d'
initial_date = '2020-12-20'
final_date = '2025-12-20'
initial_value = 1000000
desconting_value = 1000000

date_i = datetime.strptime(initial_date, fmt)
date_f = datetime.strptime(final_date, fmt)

all_months = floor(((date_f - date_i) / 30).days)
month_value = initial_value / all_months

for m in range(1, all_months + 1):
    desconting_value -= month_value
    next_month = date_i + relativedelta(months=m)
    print(f"{next_month.day}/{next_month.strftime('%m')}/{next_month.year}")
    print(f'Discounted value: {month_value:.2f}')
    print(f'Rest value: {desconting_value:.2f}')
    print()
