import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or (max - min + 1) < quantity:
        return []
    
    numbers = []
    while len(numbers) < quantity:
        number = random.randint(min, max)
        if not number in numbers:
            numbers.append(number)
    
    return sorted(numbers)
        
    
print(get_numbers_ticket(5, 40, 10))   
print(get_numbers_ticket(5, 13, 10)) 
        