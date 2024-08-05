user_input = input()
hourly_temperature = user_input.split()

''' Your solution goes here '''

for i in range(0, len(hourly_temperature)):
    print(hourly_temperature[i], end=" -> " if hourly_temperature[i + 1]  else "")
print("")