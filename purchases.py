import pandas as pd

class Purchases:
    def __init__(self):
        self.df = pd.read_csv('var5.csv')

    def __neg__(self):
        self.df_clear = self.df.drop_duplicates()
        self.df_clear.to_csv('clear.csv', index=False) # чистый от дубликатов

    def number_of_duplicates(self):
        print(f'Кличество дубликатов: {len(self.df) - len(self.df_clear)}')
    
    def bad_sort(self, file_name):
        df = pd.read_csv(file_name)
        df_minsk = df.loc[df['Место оплаты'] == 'Минск']
        df_minsk.to_csv('minsk.csv', index=False) # покупки в Минске
        df_other = df.loc[df['Место оплаты'] != 'Минск']
        df_other.to_csv('other.csv', index=False) # покупкм не в Минске

    
    def __del__(self):
        print('del done')
