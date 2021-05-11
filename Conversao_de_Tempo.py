n = int(input())

if n <= 3600:
    hours = int(n/3600)
    minutes = int(n/60)
    seconds = int(n % 60)

else:
    hours = int(n/3600)
    minutes = int((n-(hours*3600))/60)
    seconds = int(n % 60)

print('{}:{}:{}'.format(hours, minutes, seconds))