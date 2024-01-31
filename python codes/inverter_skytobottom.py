arquivo_entrada = 'D:/Gabriel/AUXILIO_AO_DELFT/dados_casan/batimetriaxyz/1055029_ENGEPLUS_RIO TAVARES_BATIMETRIA_BAIA SUL_WGS84_UTM22S_REVA_V1.XYZ'
arquivo_saida= '../finaltcc/bati_casanepagri.xyz'
import time

print('Comecei')
#abrindo os arquivos de entrada e saida
with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
    #para cada linha do arquivo, se o valor de batimetria for 0 (ou outro valor de interesse), ele vai excluir esse valor no novo arquivo
    for linha in entrada:
        #separando a linha 
        linha2=linha.split(' ')
        
        x, y, z =linha2[0], linha2[1], linha2[2]
      
        #escrevendo as variaveis arredondadas no novo arquivo usando um f-string
        linhasaida= f'{x} {y} -{z}\n'
        saida.write(linhasaida)
print('terminei')
