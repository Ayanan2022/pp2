import datetime
date_format = '%Y-%m-%d %H:%M:%S'
date1=input()
date2= input()
new_date1=datetime.datetime.strptime(date1 , date_format)
new_date2=datetime.datetime.strptime(date2 , date_format)
difference = new_date2 - new_date1
print(difference.total_seconds())

# output 
# 2025-02-15 14:30:00
# 2025-02-16 15:30:00
# 90000.0