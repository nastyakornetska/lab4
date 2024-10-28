'''start_money = 25000  
uah_vidsotok = 11.5  
usd_vidsotok = 4 
kurs_dollar1 = 27  
kurs_dollar2 = 28.6 

final_uah = start_money * (1 + uah_vidsotok / 100)

start_money_usd = start_money / kurs_dollar1  
final_usd = start_money_usd * (1 + usd_vidsotok / 100) 
final_usd_in_uah = final_usd * kurs_dollar2 

if final_uah > final_usd_in_uah:
    print(f"Вигідніше зробити внесок у гривнях: {final_uah:.2f} грн.")
else:
    print(f"Вигідніше зробити внесок у доларах: {final_usd_in_uah:.2f} грн.") '''


# завдання 2
'''
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

if a == b == c:
    print(3)  
elif a == b or a == c or b == c:
    print(2)  
else:
    print(0)  

'''


# завдання 3
'''
age = int(input("Введіть кількість років: "))

if age < 6:
    print("Ще не школяр")
elif 6 <= age <= 9:
    print("Початкова школа")
elif 10 <= age <= 15:
    print("Середня школа")
elif 16 <= age <= 17:
    print("Старша школа")
else:
    print("Вже не школяр")
'''


# завдання 4
'''
bracket = input("Введіть символ дужки: ")

if bracket == '(' or bracket == ')':
    print("Кругла дужка")
elif bracket == '[' or bracket == ']':
    print("Квадратна дужка")
elif bracket == '{' or bracket == '}':
    print("Фігурна дужка")
elif bracket == '<' or bracket == '>':
    print("Кутова дужка")
else:
    print("Це не дужка")
'''    

# завдання 4

'''schedule = {
    1: {  
        "Понеділок": ["Математика", "Фізика", "Англійська"],
        "Вівторок": ["Інформатика", "Хімія", "Фізкультура"],
        "Середа": ["Біологія", "Географія", "Історія"],
        "Четвер": ["Література", "Фізика", "Математика"],
        "П'ятниця": ["Інформатика", "Хімія", "Біологія"]
    },
    2: { 
        "Понеділок": ["Фізкультура", "Математика", "Історія"],
        "Вівторок": ["Фізика", "Хімія", "Англійська"],
        "Середа": ["Інформатика", "Географія", "Фізика"],
        "Четвер": ["Біологія", "Математика", "Література"],
        "П'ятниця": ["Хімія", "Історія", "Фізкультура"]
    }
}

week_number = int(input("Введіть номер тижня (1 або 2): "))
day_name = input("Введіть назву дня тижня (Понеділок, Вівторок, Середа, Четвер, П'ятниця): ")
    
if week_number in schedule:
    week_schedule = schedule[week_number]
        
    if day_name in week_schedule:
        day_schedule = week_schedule[day_name]
        print(f"Розклад на {day_name} ({week_number}-й тиждень): " + ", ".join(day_schedule))
    else:
        print("Неправильна назва дня тижня.")
else:
    print("Неправильний номер тижня.") '''

#завдання 6
'''
a = float(input("Введіть довжину першої сторони: "))
b = float(input("Введіть довжину другої сторони: "))
c = float(input("Введіть довжину третьої сторони: "))

if a + b > c and a + c > b and b + c > a:
    if a==b==c:
        print("Це рівносторонній трикутник")
    elif a == b != c or a == c != b or b == c != a:
        print("Це рівнобедрений трикутник")
    elif a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print("Це прямокутний трикутник")
    else: print("Це довільний трикутник")
else:
    print("Трикутник не існує.")'''

#завдання 7
a = int(input("Введіть двозначне число: "))
b=a%10
c=a//10
if b<6 and c<6:
    print("Істинність справджується: кожна цифра числа менша 6")
elif b>=6 or c>=6: 
    print("Істинність несправджується")