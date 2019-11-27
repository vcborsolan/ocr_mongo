# Projeto feito para materia de Banco de dados avançados no curso de ADS unimar/2019

## Dependecias:

sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-[por]
instalar homebrew
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
pip install pillow
pip install wand
brew install imagemagick@6
brew unlink imagemagick
brew link imagemagick@6 --force
pipenv install
pipenv shell
flask run

mongo:
startar imagem do mongo --> sudo docker start af7a7bdcf313
entrar do shell do docker mongo --> sudo docker exec -i af7a7bdcf313 
o mongo esta sendo redirecionado portas --> 0.0.0.0:27017->27017/tcp, 0.0.0.0:28017->28017/tcp
O mongo esta sem senha
tutorial do mongo q estou usando --> https://medium.com/dockerbr/mongodb-no-docker-dd3b72c7efb7
senha do mongo usuario -> admin senha -> oJ8FEc8Jv0BX