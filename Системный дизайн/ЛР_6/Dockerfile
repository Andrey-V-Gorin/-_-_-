# our base image

#docker build . -t my_nginx
#docker images
#docker run --rm -p 80:80 -i my_nginx

FROM python:3.9
WORKDIR /app
COPY settings.txt .
RUN pip3 install --no-cache-dir -r settings.txt
COPY ./app /app
CMD ["python", "run.py"]
