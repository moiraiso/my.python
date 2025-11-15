import os
from PIL import Image

try:
    for file in os.listdir():
        if file.split('.')[-1] in ('jpeg', 'jpg', 'png'):
            file_name = os.path.basename(file).split('.')[-2]
            imagem = Image.open(file)
            imagem_convertida = imagem.convert('RGB')
            imagem_convertida.save('{0}.pdf'.format(file_name))
except:
    print('Erro na Execução!')
finally:
    print('Arquivos Salvos com sucesso!')