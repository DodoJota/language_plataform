# Usa a imagem oficial do Python como base
FROM python:3.12

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do Django (por padrão, 8000)
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["gunicorn", "plataforms.wsgi:application", "--bind", "0.0.0.0:8000"]
