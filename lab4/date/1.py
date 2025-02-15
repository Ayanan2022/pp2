import datetime
x=datetime.datetime.now()
five_days=datetime.timedelta(days=5)
rslt=x-five_days
print(rslt.strftime("%a"))