From python:3.9-slim

WORKDIR /app

COPY requirements.txt  .

RUN pip install --upgrade pip && pip install  -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "main:app" , "--access-logfile" , "access.log" , "--error-logfile" , "error.log"]
