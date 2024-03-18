arquivo_entrada = "../finaltcc/altimetria/altimetria_rtavares_semrio_alteradaprajunntar.xyz"
arquivo_aux = '../finaltcc/batimetria/bati_flripa_32722_casanepagri_corrigido_imbituba.xyz'
arquivo_saida= '../finaltcc/bati_altimetria/altibati_flp_32722.xyz'

print('comecei')

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
print('terminou')
arquivo_final.close()