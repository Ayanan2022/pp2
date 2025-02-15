import datetime
current = datetime.datetime.now()
answer = current.replace(microsecond=0)
print(answer)