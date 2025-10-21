# Usa imagem base do Python
FROM python:3.11-slim

# Define diretório de trabalho no container
WORKDIR /app

# Copia os arquivos da aplicação
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pelo Flask
EXPOSE 5000

# Comando para iniciar o app
CMD ["python", "app.py"]
