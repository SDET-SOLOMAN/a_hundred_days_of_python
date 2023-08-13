def year(time, month):
    months = [31, 28, 30, 31, 30, 31]
    if time:
        return months[month - 1] + 1
    return months[month - 1]

print(year(True, 2))