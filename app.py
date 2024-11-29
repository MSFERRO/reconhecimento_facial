from flask import Flask, render_template, request, url_for
import os
from datetime import datetime
from PIL import Image
from reconhecimento import processar_reconhecimento_facial  # Função de reconhecimento facial

app = Flask(__name__)

# Configura o caminho para salvar imagens processadas
IMAGES_DIR = os.path.join('static', 'imagens')
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

@app.route('/')
def index():
    """
    Página inicial com o formulário de upload.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    """
    Rota para lidar com o upload de imagens e processar o reconhecimento facial.
    """
    if 'file' not in request.files:
        return render_template('index.html', mensagem="Nenhum arquivo foi enviado.")
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', mensagem="Nenhum arquivo selecionado.")
    
    try:
        # Valida o tipo MIME do arquivo
        if not file.content_type.startswith('image/'):
            return render_template('index.html', mensagem="Por favor, envie um arquivo de imagem.")

        # Verifica se é uma imagem válida
        img = Image.open(file)
        img.verify()  # Checa se é uma imagem válida
        
        # Salva a imagem original com um nome único
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
        file_path = os.path.join(IMAGES_DIR, filename)
        file.seek(0)  # Volta ao início do arquivo para salvá-lo
        img = Image.open(file)  # Reabre a imagem para salvamento
        img.save(file_path)

        # Realiza o reconhecimento facial
        resultado = processar_reconhecimento_facial(file_path)

        # Gera a URL da imagem processada
        imagem_processada_url = url_for('static', filename=f'imagens/{filename}')

        return render_template('index.html', mensagem=resultado, imagem_processada=imagem_processada_url)
    
    except Exception as e:
        # Captura erros e exibe uma mensagem informativa
        return render_template('index.html', mensagem=f"Erro: O arquivo não é uma imagem válida ou ocorreu um problema. ({str(e)})")

if __name__ == '__main__':
    app.run(debug=True)