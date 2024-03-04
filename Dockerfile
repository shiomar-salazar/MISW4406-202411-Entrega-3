FROM python:3.9
ENV PYTHONUNBUFFERED 1
EXPOSE 5000/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "./src/propiedadesalpes/api", "--debug", "run", "--host=0.0.0.0"]