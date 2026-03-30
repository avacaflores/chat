FROM python:3.9-slim

WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Clone the repository
RUN git clone https://github.com/avacaflores/chat.git .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]