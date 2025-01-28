# Utilizando a imagem do nginx com a versão alpine como imagem base
FROM nginx:1.25.4

WORKDIR /app

# Copiando os arquivos do diretório src para o diretório html do nginx
# LINK: https://askubuntu.com/questions/873839/what-is-the-www-data-user
COPY --chown=www-data ./src/ /app

# Copiando o arquivo default.conf para o diretório de configuração do nginx
# LINK: https://askubuntu.com/questions/873839/what-is-the-www-data-user
COPY --chown=www-data ./default.conf /etc/nginx/conf.d/default.conf

# Expondo a porta 8000
EXPOSE 8000