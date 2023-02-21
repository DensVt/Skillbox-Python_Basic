class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"День: {self.day} Месяц: {self.month} Год: {self.year}"
    
    
    @staticmethod
    def from_string(date_str):
        if not Date.is_valid_date(date_str):
            raise ValueError("Неверный формат даты")
        day, month, year = map(int, date_str.split('-'))
        return Date(day, month, year)


    @staticmethod
    def is_valid_date(date_str):
        try:
            day, month, year = map(int, date_str.split('-'))
            if day < 1 or day > 31:
                return False
            if month < 1 or month > 12:
                return False
            if year < 1:
                return False
            if month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    if day > 29:
                        return False
                else:
                    if day > 28:
                        return False
            elif month in [4, 6, 9, 11]:
                if day > 30:
                    return False
            return True
        except:
            return False

    

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_valid_date('10-12-2077'))
print(Date.is_valid_date('40-12-2077'))