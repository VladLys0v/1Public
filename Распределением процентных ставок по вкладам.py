#Задание: 
#1-распределить процентные ставки по вкладам в банках
#2-сформировать список накопленных средств в каждом банке
#3-найти максимальное значение среди элементов в списке и представить его как наиболее доходный вариант

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int( input('Please enter the deposit amount:'))
deposit_term = int(input ("Please eneter the term of the deposit in days (1 year = 365 days):"))
#добавил переменнуй deposit_term = ввод с клавиатуры срока депозита
#deposit_term позволяет считать и для года и для меньшего и ли большего срока
#формула дохода по вкладу на произвольный срок = D
#D = депозит * размер годовой процентной ставки * количество дней, на которые размещается вклад / количество дней в году
deposit = [per_cent.get('ТКБ')* money * deposit_term / 365,per_cent.get('СКБ')* money * deposit_term / 365,
           per_cent.get('ВТБ')* money * deposit_term / 365,per_cent.get('СБЕР')* money * deposit_term / 365]
deposit_round=[round(v,3) for v in deposit]
deposit_max = max(deposit)
print (deposit_round)
print("Наиболее доходный вариант:",round(deposit_max,3))