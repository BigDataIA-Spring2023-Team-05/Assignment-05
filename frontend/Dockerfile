FROM python:3.10.6

RUN pip install --upgrade pip

WORKDIR /frontend

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "PromaA.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableWebsocketCompression=false"]