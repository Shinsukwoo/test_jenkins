# ./Dockerfile
FROM python
WORKDIR /usr/src/app

# install package
COPY requirements.txt ./
RUN pip install -r requirements.txt

## Copy all src files
COPY . .

## Run the application on the port 8080
EXPOSE 8000

# GUNICORN 배포 명령어
# CMD ["gunicorn","--bind", "허용하는 IP:열어줄 포트", "project.wsgi:application"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stock.wsgi:application"]