# Биржевой Джин - биржевой калькулятор и справочник.
print ('Приветствую тебя, это Биржевой Джин версии 0.01')
print ('Автор: Дмитрий Моргало. 15.10.2020 год')
print ('Задай индекс акций:')
AFLT = ('Аэрофлот')
AFLTl = ('1 декабря 2010 года')
AFLT_max = 201.7
AFLT_min = 49
AFLT_div = ('май или июль')
stock = input()
print ('----------------------------')
if (stock == 'AFLT'):
  print ('Название:', AFLT)
  print ('Листинг на бирже:', AFLTl)
  print ('Максимальное значение:', AFLT_max)
  print ('Минимальное значение:', AFLT_min)
  print ('Среднее значение:', (AFLT_max + AFLT_min)/2 )
  print ('Дивиденды:', AFLT_div)
  print ('----------------------------')
else:
  print ('Попробуй еще раз')
stock_cost = float(input('Введи стоимость акции: '))
percent_dealer = float(input('Введи комиссию за покупку в %: '))
bank = float(input('Сумму покупки: '))
print ('Можно купить:', (bank - ( bank * (percent_dealer / 100))) / stock_cost , 'акций'  )
print ('или')
print ('----------------------------') 
bank10 = bank / 10
s = 0
stock_cost1 = stock_cost
stocks_all = 0
stock_cost2 = 0
while s <= 9:
  s = s+1
  stock_cost1 = stock_cost1 - (stock_cost / 100)
  stocks = (bank10 - ( bank10 * (percent_dealer / 100))) / stock_cost1
  stocks_all = stocks + stocks_all
  stock_cost2 = stock_cost1 + stock_cost2
  print ( stocks, 'по цене', stock_cost1 )
print ('----------------------------') 
print ('Купить лесенкой:') 
print (stocks_all, 'по цене', stock_cost2 / 10 )
print ('----------------------------') 
print ('Заработок 5% при цене:', stock_cost2 / 10 + (( stock_cost2 / 1000 ) * (5 + percent_dealer )) )
print ('Заработок в рублях:', ((stock_cost2 / 10 + (( stock_cost2 / 1000 ) * (5 + percent_dealer ))) * stocks_all) - bank )  
print ('Заработок 10% при цене:', stock_cost2 / 10 + (( stock_cost2 / 1000 ) * (10 + percent_dealer )) ) 
print ('Заработок в рублях:', ((stock_cost2 / 10 + (( stock_cost2 / 1000 ) * (10 + percent_dealer ))) * stocks_all) - bank ) 