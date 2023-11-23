# Imagem a ser utilizada
FROM python:3.10.6

# Diretório onde a aplicação vai ficar
WORKDIR /app

# Variáveis de ambiente para a execução do container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalação das dependências
COPY requirements.txt .

# Copiando o resto do código fonte para o container
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
# RUN python3 manage.py collectstatic
RUN ./manage.py collectstatic

# Executando o gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]