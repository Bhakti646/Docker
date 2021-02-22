FROM gcc:10.2.0
WORKDIR /usr/src/capp
#LABEL maintainer= "Bhakti"
COPY code.c .
RUN gcc -o code code.c
CMD ["./code"]
