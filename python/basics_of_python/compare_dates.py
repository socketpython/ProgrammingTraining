import  datetime


currentDate = datetime.date.today()
dp = input('enter your deadline date (dd/mm/yy) ')
date = datetime.datetime.strptime(dp, '%d/%m/%y').date()
difference = date - currentDate
print(f'you got {difference.days} days to your deadline')
