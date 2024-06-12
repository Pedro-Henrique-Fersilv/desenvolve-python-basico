import datetime

data = datetime.datetime.now()
data_formatada = data.strftime('%d/%m/%Y')
hora = data.strftime('%H:%M')

print("Data:", data_formatada)
print("Hora", hora)