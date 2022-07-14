FROM python # base image

COPY start.sh /start.sh # copied the startup script 

EXPOSE 8000 # exposed port 8000 to allow its communication to and from the server

CMD ["/start.sh"] # command to be executed to start the server