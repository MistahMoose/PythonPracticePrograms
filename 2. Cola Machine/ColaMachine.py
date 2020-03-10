#! python3

print('Please Choose your Favorite Beverage')
print('1.Coke 2.Water 3.Sprite 4.Drpep 5.Lemonade')

vendingNum = int(input())

if vendingNum == 1:
	print('Here is your Coke! KACHINK')
elif vendingNum == 2:
	print('Here is your Water! KACHINK')
elif vendingNum == 3:
	print('Here is your Sprite! KACHINK')
elif vendingNum == 4:
	print('Here is your Drpep! KACHINK')
elif vendingNum == 5:
	print('Here is your Lemonade! KACHINK')
elif vendingNum < 0 or vendingNum > 5:#Would prefer to encapsulate this in a while loop, but following the practice.
	print('Sorry, Invalid input. Here is your money back')
