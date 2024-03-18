from PIL import Image

# Carregar a carta náutica em formato TIFF
carta_tiff = Image.open('190201.TIF')

# Exibir informações sobre a imagem
print(carta_tiff.format, carta_tiff.size, carta_tiff.mode)

# Mostrar a imagem
carta_tiff.show()