#importando os arquivos xyz e criando um arquivo novo de saida, com o proposito de diminuir o arquivo gigantesco de 62gibas
#escrevaaqui o local
local= 'norte'

dado_modelo = f'maregrafo{local}.csv'
dado_processado = f'maregrafo{local}_processado.csv'
import time

print('Comecei')
#abrindo os arquivos de entrada e saida
with open(dado_modelo, 'r') as modelo, open(dado_processado, 'w') as proces :
    proces.write('data,nivel\n')
    #para cada linha do arquivo, vou arrumar valores de data, hora e maré
    for linha in modelo:
        linha2=linha.split(' ')
        #arrumando hora, excluindo o valor de segundos que não era usado.
        hm_sep = linha2[1].split(',')
        tempo = hm_sep[0].split(':')
        tempopronto= f'{tempo[0]}:{tempo[1]}'
        #arrumando valores de maré
        marepronta= hm_sep[1].replace('_', '.')
        #escrevendo os dados processados em um novo arquivo:
        proces.write(f'{linha2[0]} {tempopronto},{marepronta}')

print('Terminei')

