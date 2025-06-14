# 1 завдання
from datetime import datetime

def get_days_from_today(date):
    try:
        return (datetime.today() - datetime.strptime(date,"%Y-%m-%d")).days
    except ValueError:
        return "Введіть дату у форматі 'YYYY-MM-DD'"

# 2 завдання
import random

def get_numbers_ticket(min, max, quantity):
    try:
        tickets_set = set()
        empty_list = []
        if quantity > (max - min + 1) or min > max or min < 1 or max > 1000 :
            return empty_list
        else:
            while len(tickets_set) < quantity:
                tickets_set.add(random.randint(min, max))
            sorted_set = sorted(tickets_set)
            return sorted_set
    except ValueError:
        return empty_list

# 3 завдання
import re

def normalize_phone(phone_number):
    normal_number = re.sub(r"\D","", phone_number)
    match_1 = re.search(r"^38\d+", normal_number)
    if match_1:
        return "+" + normal_number
    else:
        return "+38" + normal_number

