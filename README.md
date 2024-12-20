# Reconhecimento Facial - Flask Image Capture Application

Este é um projeto simples de captura e reconhecimento facial utilizando Flask, OpenCV e a biblioteca `face_recognition`. O aplicativo permite que os usuários façam upload de imagens, capturem fotos via câmera e detectem rostos nas imagens enviadas.

## Funcionalidades

- **Captura de Imagem**: Permite capturar uma imagem diretamente da câmera do dispositivo (em navegadores compatíveis).
- **Upload de Imagem**: Permite o upload de arquivos de imagem para análise.
- **Reconhecimento Facial**: Detecta e destaca faces presentes nas imagens enviadas.
- **Armazenamento de Imagens**: Salva as imagens capturadas ou enviadas no diretório `imagens/` com nomes únicos.

## Tecnologias Utilizadas

- **Flask**: Framework web leve para desenvolvimento do servidor.
- **OpenCV**: Biblioteca para processamento de imagens e vídeos.
- **face_recognition**: Biblioteca para detecção e reconhecimento facial.
- **Pillow (PIL)**: Biblioteca para manipulação de imagens.
- **Python 3.x**: Linguagem de programação principal.

## Requisitos

- **Python 3.x**
- Bibliotecas **Flask**, **Pillow**, **OpenCV** e **face_recognition** (instaladas via `pip`).

## Como Rodar o Projeto

### 1. Clonar o Repositório

Clone o repositório para a sua máquina local:

```bash
git clone git@github.com:MSFERRO/reconhecimento_facial.git
cd reconhecimento_facial
```

### 2. Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)

Para isolar as dependências do projeto, utilize um ambiente virtual:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências

Instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

> Caso não tenha o arquivo `requirements.txt`, instale manualmente:
```bash
pip install Flask Pillow opencv-python face_recognition
```

### 4. Executar o Servidor

Inicie o servidor Flask com o comando:

```bash
python app.py
```

O servidor estará acessível em [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 5. Acessar a Aplicação

Abra seu navegador e acesse [http://127.0.0.1:5000](http://127.0.0.1:5000). Você poderá capturar imagens, fazer upload e visualizar as faces detectadas.

## Estrutura do Projeto

```plaintext
/reconhecimento facial
│
├── app.py                  # Código principal do Flask
├── reconhecimento.py       # Código de reconhecimento facial
├── templates/
│   └── index.html          # Template HTML
├── static/
│   └── imagens/            # Diretório para armazenar imagens enviadas e processadas
└── requirements.txt        # Dependências do projeto

```

## Como Funciona

1. O usuário acessa a interface web e envia uma imagem ou tira uma foto diretamente da câmera.
2. O servidor Flask processa a imagem usando as bibliotecas **OpenCV** e **face_recognition**.
3. As faces detectadas são destacadas na imagem, que é exibida de volta ao usuário e armazenada no diretório `imagens/`.

## Contribuindo

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nome-da-feature
   ```
3. Comite suas mudanças:
   ```bash
   git commit -m 'Adicionando nova funcionalidade'
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin feature/nome-da-feature
   ```
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a **MIT License**. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

## Contato

- **Autor**: Seu Nome  
- **E-mail**: seu_email@example.com  
- **GitHub**: [seu_usuario](https://github.com/seu_usuario)  

