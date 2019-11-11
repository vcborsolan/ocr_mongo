<!-- instalar o tesseract no computador , fora do virtualenv -->
sudo apt-get install tesseract-ocr
<!-- instalar o modelo de analise da linguagem portugues -->
sudo apt-get install tesseract-ocr-[por]
<!-- instalar as dependencias do projeto -->
pipenv install
<!-- entrar no virtualenv para rodar projeto -->
pipenv shell
<!-- rodar servidor padrão porta :5000 -->
flask run