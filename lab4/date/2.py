import datetime
x=datetime.datetime.today()
a=datetime.timedelta(days=1)
ystd=x-a
tmw=x+a
print(ystd.strftime('%A'),x.strftime('%A'),tmw.strftime('%A'))