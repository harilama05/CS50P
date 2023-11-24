def main():
    time = input("What time is it? ").strip()
    print(convert(time))
def convert(time):
    hour, minute = time.split(":")
    hour = float(hour) + float(minute)/60    
    if 7<=hour<=8:
        return "breakfast time"
    elif 12<=hour<=13:
        return "lunch time"
    elif 18<=hour<=19:
        return "dinner time"
if __name__ == "__main__":
    main()