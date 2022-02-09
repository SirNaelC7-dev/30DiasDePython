from datetime import datetime, timedelta

dados_agora = datetime.now()

dia = dados_agora.day
mes = dados_agora.month
ano = dados_agora.year

hora = dados_agora.hour
minuto = dados_agora.minute
carimbo_data_hora = dados_agora.timestamp()

print(f'{dia} de {mes} de {ano} - {hora}:{minuto} ')
print(f'carimbo data_hora: {carimbo_data_hora}')


time_one = dados_agora.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)

data_atual = datetime(year=ano, month=mes, day=dia)
proxim_ano = datetime(year=2023, month=1, day=1)
diferenca = proxim_ano - data_atual

data = datetime(year=1970, month=1, day=1)
agora = datetime(year=ano, month=mes, day=dia)
diferenca = (agora - data) / timedelta(hours=1)
