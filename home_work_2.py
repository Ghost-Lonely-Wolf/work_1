time = int(input('Введите пятизначное число '))
def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%02d:%02d:%02d" %(hour, min, sec)
print(convert(time))