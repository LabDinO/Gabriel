#importando os arquivos xyz e criando um arquivo novo de saida, com o proposito de diminuir o arquivo gigantesco de 62gibas
local='norte'


dado_medido = f'maregrafo{local}_medido.csv'
dado_processado = f'maregrafo{local}_medido_processado.csv'
import time

print('Comecei')
#abrindo os arquivos de entrada e saida
with open(dado_medido, 'r') as medido, open(dado_processado, 'w') as proces :
    

    proces.write('data,nivel\n')
    #para cada linha do arquivo, vou arrumar valores de data, hora e maré
    for linha in medido:
        linha2=linha.split(' ')
        #arrumando data de "MM/DD/AAAA" para "AAAA/MM/DD"
        datasplit=linha2[0].split('/')
        if int(datasplit[2])>19 and int(datasplit[1])<19:
            datapronta= f'20{datasplit[2]}/{datasplit[0]}/{datasplit[1]}'
        #arrumando a hora, de sistema estaduniense para o correto.
            tempo= linha2[1].split(':')
            hm_sep = linha2[2].split(';')
            tempocerto= int(tempo[0])
            if tempocerto>= 12:
                tempocerto -=12
            if hm_sep[0]=='PM':
                tempocerto += 12
            tempopronto= f'{tempocerto}:{tempo[1]}'
        #arrumando valores de maré de ',' para '.'
            marepronta= hm_sep[1].replace(',', '.')
        #escrevendo os dados processados em um novo arquivo:
            proces.write(f'{datapronta} {tempopronto},{marepronta}')

print('Terminei')

