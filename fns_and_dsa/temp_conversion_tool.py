FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    CELSIUS_TO_FAHRENHEIT_FACTOR
    answer = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return answer

def main():
    temp = float(input(f"Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    
    # if temp:
    #     if unit == "F":
    #         conv_unit = convert_to_celsius(temp)
    #         print(f"{temp}°F is {conv_unit}°C")
    #     elif unit == "C":
    #         conv_unit = convert_to_fahrenheit(temp)
    #         print(f"{temp}°C is {conv_unit}°F")
    #     # else:
    #         # print("Run the program again and Choose a valid option(C/F)!")
    # # else:
    #     print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
