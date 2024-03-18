arquivo_entrada = '../finaltcc/batimetria/batimetria_floripa_32722_wgs84_casanepagri.xyz'
arquivo_saida= '../finaltcc/batimetria/bati_flripa_32722_casanepagri_corrigido_imbituba.xyz'
import time

print('Comecei')
#abrindo os arquivos de entrada e saida
with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
    #para cada linha do arquivo, se o valor de batimetria for 0 (ou outro valor de interesse), ele vai excluir esse valor no novo arquivo
    for linha in entrada:
       
        #separando a linha 
        linha2=linha.split(' ')

        #criando variaveis para arredondar os numeros
        x, y, z =float(linha2[0]), float(linha2[1]), float(linha2[2])
        #variaveis arredondadas
        
        rx, ry, rz = round(x, 3), round(y, 3), round(z+0.4, 4)
        
        #escrevendo as variaveis arredondadas no novo arquivo usando um fstring
        linhasaida= f'{rx} {ry} {rz}\n'
        saida.write(linhasaida)
print('terminei')