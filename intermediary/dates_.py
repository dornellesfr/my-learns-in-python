from datetime import datetime, timedelta
from pytz import timezone


date_str = '2022-04-20 07:49:23'
date_br = '20/04/2022'

fmt = '%Y-%m-%d %H:%M:%S'
date_br_format = '%d/%m/%Y'

date = datetime(2023, 7, 4, 7, 7, 59, tzinfo=timezone('Asia/Tokyo'))

transform_date = datetime.strptime(date_br, date_br_format)
# Converte a data de string para um objeto datetime

print(transform_date)
print(datetime.now(timezone('Asia/Tokyo')))

# Timestamps:
new_date = datetime.now()
time_stamp = new_date.timestamp()  # Guarda a data em forma de timestamp
print(datetime.fromtimestamp(time_stamp))  # Convert o timestamp para data atua

# ---------------------------------------------------------------------
fmt_br = '%d/%m/%Y %H:%M:%S'

initial_date = datetime.strptime('20/04/1987 09:30:30', fmt_br)
end_date = datetime.strptime('12/12/2022 08:20:20', fmt_br)

print(initial_date > end_date)
print(end_date > initial_date)
print(initial_date == end_date)
print(end_date - initial_date)  # Timedelta das datas (diferença)

delta = timedelta(days=10, hours=20, seconds=12, minutes=30)
extended_end = end_date + delta
reduced_end = end_date - delta
print(reduced_end)
print(extended_end)
