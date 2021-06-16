import datetime

def CalculaResina(hora, resin_atual, resin):
  dif = abs(resin - resin_atual)
  result = dif * 8
  hora += datetime.timedelta(minutes=result)
  return "{:02d}:{:02d}".format(hora.hour, hora.minute)

def getInt(message):
  value = abs(int(input(message)))
  if(value > 160):
    value = 160
  return value

while(True):
  resin_atual = getInt("Insira sua quantidade de resina: ")
  print("Sua resina: ", resin_atual)
  resin = getInt("Insira a resina desejada(MAX: 160): ")
  print("Resina desejada: ", resin)
  hora_atual = datetime.datetime.now()

  complete_in = CalculaResina(hora_atual, resin_atual, resin)

  print("Sua resina ", resin_atual, " estará recarregada para ", resin, " às: ", complete_in, " horas.")
  if input("Insira '-1' para sair ou só pressione Enter para calcular de novo...") == '-1':
    break
