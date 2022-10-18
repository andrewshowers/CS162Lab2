userinput = input('please enter the amount of seconds you would like converted')
userinput = (int(userinput))
hours = userinput//3600
userinput %= 3600
minutes = userinput//60
userinput %= 60
seconds = userinput
print(hours, 'hour(s)')
print(minutes, 'minute(s)')
print(seconds, 'second(s)')
