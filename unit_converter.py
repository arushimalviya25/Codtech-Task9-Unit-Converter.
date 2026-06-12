def convert_distance():
    print("\n--- Distance Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Select (1 or 2): ")
    value = float(input("Enter value: "))
    
    if choice == '1':
        print(f"{value} KM = {value * 0.621371:.2f} Miles")
    elif choice == '2':
        print(f"{value} Miles = {value / 0.621371:.2f} KM")

def convert_temperature():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Select (1 or 2): ")
    value = float(input("Enter value: "))
    
    if choice == '1':
        print(f"{value}°C = {(value * 9/5) + 32:.2f}°F")
    elif choice == '2':
        print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")

def main():
    while True:
        print("\n=== UNIT CONVERTER ===")
        print("1. Distance")
        print("2. Temperature")
        print("3. Exit")
        choice = input("Choose category: ")
        
        if choice == '1':
            convert_distance()
        elif choice == '2':
            convert_temperature()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()