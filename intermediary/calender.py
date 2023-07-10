import calendar

# print(calendar.calendar(2023, 12)) Mostra o calendário do ano/mês

# print(calendar.monthrange(2023, 7))

# Primeiro valor é o dia da semana do
# primeiro dia do mês
# Segundo valor é o último dia do mês

first_day, _a = calendar.monthrange(2000, 12)


def get_weekday(number: int):
    return calendar.day_name[number]


# print(calendar.day_name[first_day])
# Usa a lista de dias da semana para mostr

print(get_weekday(calendar.weekday(2022, 12, 18)))
