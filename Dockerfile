FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python process_data.py

EXPOSE 5000

CMD ["python", "main.py"]