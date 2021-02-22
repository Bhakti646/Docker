FROM centos:7
LABEL devloper="bhakti"
RUN yum -y update hhtpd
RUN yum -y install httpd
#default file for index in apache sever
COPY index.html /var/www/html
#start your http server in background
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
#run the server at the port 80 inside container
EXPOSE 80 
