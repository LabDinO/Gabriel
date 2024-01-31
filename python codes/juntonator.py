arquivo_entrada = "../finaltcc/batimetria/bati_casanepagri2.xyz"
arquivo_aux = 'dados_casan/batimetriaxyz/1055029_ENGEPLUS_RIO TAVARES_BATIMETRIA_TRECHO2_BRAÇO NORTE_UTM22S_WGS84_REVA_V1.XYZ'
arquivo_saida= '../finaltcc/batimetria/bati_casanepagri_final.xyz'


# Abra os arquivos de entrada e saída
with open(arquivo_entrada, 'r') as arquivo1, open(arquivo_aux, 'r') as arquivo2, open(arquivo_saida, 'w') as arquivo_final:
    # Lê o conteúdo do primeiro arquivo e escreve no arquivo de saída
    for linha in arquivo1:
        arquivo_final.write(linha)
    
    # Lê o conteúdo do segundo arquivo e escreve no arquivo de saída
    for linha in arquivo2:
        arquivo_final.write(linha)

# Feche os arquivos
arquivo1.close()
arquivo2.close()
print('oi')
arquivo_final.close()