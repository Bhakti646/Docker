FROM python:3.8-alpine
LABEL maintainer="diot2020"
WORKDIR /usr/src/app
COPY app.py /usr/src/app
COPY requirement.txt /usr/src/app
# COPY . /usr/src/app
RUN pip3 install -r requirement.txt
EXPOSE 4500
CMD ["python3","app.py"]


