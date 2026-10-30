# https://github.com/asalnorouzzade/Practice-30-AVG.git
def average(numbers):
    return sum(numbers) / len(numbers)

while True:
    text = input()
    parts = text.split()
    is_valid = True
    numbers = []
    
    for part in parts:
        try:
            num = float(part)
            numbers.append(num)
        except ValueError:
            is_valid = False
            break
            
    if is_valid and len(numbers) > 0:
        avg = average(numbers)
        print(f"{avg:.2f}")
        break
      
    else:
        print("Invalid Input! Enter a valid input.")
