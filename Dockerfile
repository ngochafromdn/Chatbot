# app/Dockerfile

FROM python:3.9-slim
EXPOSE 80
WORKDIR /app
# dont write pyc files
# dont buffer to stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./requirements.txt
RUN pip3 install -U pip \
    && pip3 install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .
RUN chmod +x setup.sh && ./setup.sh
ENTRYPOINT ["streamlit", "run", "chatbot.py", "--server.port=80", "--server.address=0.0.0.0"]