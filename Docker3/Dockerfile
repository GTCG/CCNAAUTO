FROM  ubuntu:16.04
LABEL creator="me"
RUN apt-get update && apt-get upgrade -y
RUN apt-get install nginx -y
EXPOSE 80 443
VOLUME /sur/share/nginx/html
CMD [ "nginx","-g","daemon off;" ]