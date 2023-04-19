FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expose the port the app runs on
EXPOSE 5000

CMD ["python", "run.py"]
