import datetime as dt


class Record:
        def __init__(self, amount, comment, date=None):
            self.amount = amount
            self.comment = comment
            if type(date) is str:
                self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
            else:
                self.date = dt.date.today()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        """Add a new record. 
 
        Keyword arguments: 
        record -- object of tipe Record  
        """ 
        self.records.append(record) 
        
    def get_today_stats(self):
        """Calculate how much money or calories spent today."""
        date_today = dt.date.today()
        
        return sum(record.amount for record in self.records 
                if record.date == date_today)
        
    def get_week_stats(self):
        """Calculate how much money or calories spent last week."""
        seven_days_period = dt.timedelta(days=7)
        date_today = dt.date.today()
       
        return sum(record.amount for record in self.records 
                if date_today - seven_days_period <= record.date <= date_today)
    
    def calculate_remaind(self):
        """Calculate remaind for today""" 
        today_spend = self.get_today_stats()
        
        return self.limit - today_spend


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        """Determine how many calories can to get today."""
        remaind = self.calculate_remaind()
        
        return ('Сегодня можно съесть что-нибудь ещё,' 
                + f' но с общей калорийностью не более {remaind} кКал' 
                if remaind > 0 else 'Хватит есть!') 


class CashCalculator(Calculator):
    USD_RATE = 76.34
    EURO_RATE = 89.90
    def convert_remaind(self, currency, remaind): 
        """Do currency conversion. 
 
        Keyword arguments: 
        currency -- name currency, may be "rub", "usd" or "eur" 
 
        """ 
        exchange_rates = { 
            'usd': {'name': 'USD', 'value': self.USD_RATE}, 
            'eur': {'name': 'Euro', 'value': self.EURO_RATE}, 
            'rub': {'name': 'руб', 'value': 1} 
        } 
 
        if currency in exchange_rates: 
            remaind /= exchange_rates[currency]['value'] 
            name_currency = exchange_rates[currency]['name'] 
        else: 

            raise NameError('Unknown currency') 
 
        return remaind, name_currency 
 
    def get_today_cash_remained(self, currency): 
        """Determine how many money can to get today. 
 
        Keyword arguments: 
        currency -- name currency, may be "rub", "usd" or "eur" 
 
        """ 
        remaind = self.calculate_remaind() 
 
        if remaind == 0: 
            return 'Денег нет, держись' 
 
        remaind, currency = self.convert_remaind(currency, remaind) 
 
        if remaind > 0: 
            round_remaind = round(remaind, 2) 
            return f'На сегодня осталось {round_remaind} {currency}' 
 
        round_remaind = round(abs(remaind), 2) 
        return ('Денег нет, держись: твой долг - ' 
                + f'{round_remaind} {currency}') 
 
 
class Record: 
    def __init__(self, amount, comment, date=None): 
        self.amount = amount 
        self.date = (dt.datetime.strptime(date, '%d.%m.%Y').date() 
                     if type(date) is str else dt.date.today()) 
        self.comment = comment 



    
    