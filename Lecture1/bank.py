# Exercise ------------------------------------------------------------------------------------------------------------------
# You are developing a feature for a weather application that requires the conversion of
# temperatures from Fahrenheit to Celsius. 
# 
# Write a Python function that:
# 1) The name of the function is 'fahrenheit_to_celsius'.
# 2) Takes a temperature in Fahrenheit as input.In this scenario, 
#      the temperature in Fahrenheit is provided as a hardcoded value of 68.
# 3) Converts it to Celsius using the formula C = (F - 32) X 5/9.
# 4) The return value of the function is the result converted to Celsius.
# 5) Save the result of calling the function you wrote in the 'temp_celsius' variable.
# ===========================================================================================================================

# User input
temp_fahrenheit = 68

# Write a Python function named 'fahrenheit_to_celsius'
'''
Type Code From Here
'''
fahrenheit_to_celsius(F):
    C = (F - 32) * 5/9
    return C
  

# Save the result of calling your function in the 'temp_celsius' variable.
'''
Type Code From Here
'''

temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)

# Do not delete the code below for evaluation purposes.
print("Temperature in Fahrenheit:", temp_fahrenheit)
print("Temperature in Celsius:", temp_celsius)