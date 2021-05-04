seconds = int(input("Введите кол-во секунд: "))
hours = seconds // 3600
minutes = (seconds - (hours * 3600)) // 60
seconds = seconds - (hours * 3600 + minutes * 60)
print(f"Время в правильном формате: {hours}:{minutes}:{seconds}")