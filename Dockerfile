FROM python:3.7
LABEL maintainer="sil@permcnti.ru"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8182
EXPOSE 8181
VOLUME /app/app/models
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
