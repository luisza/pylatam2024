# Use an official Python runtime as a parent image
FROM python:3.11-bookworm
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive
ENV MEDIA_ROOT=/pylatam/media/
ENV STATIC_ROOT=/run/static/
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

ARG UID=1000
ARG GUID=1000
ENV USER="pylatam"
ENV SYSTEMGROUP="pylatam"

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nginx supervisor gettext

RUN addgroup --system --gid $GUID $SYSTEMGROUP  && \
    useradd --uid $UID  --gid $GUID --system --no-create-home $USER && \
    mkdir -p /run/logs/ /run/static/

WORKDIR /pylatam

ADD requirements.txt /pylatam

RUN pip install --upgrade --trusted-host pypi.python.org --no-cache-dir pip gunicorn && \
pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

RUN  apt-get -y autoremove --purge  && \
     apt-get -y clean   && \
     rm -rf /var/lib/apt/lists/*

RUN echo "daemon off;" >> /etc/nginx/nginx.conf && \
    sed -i 's/user www-data;/user pylatam;/g' /etc/nginx/nginx.conf

COPY docker/nginx-app.conf /etc/nginx/sites-available/default
COPY docker/supervisor-app.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker/nginx_personalize.py /pylatam/nginx_personalize.py
COPY docker/launcher.sh /run/launcher.sh
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
ADD src /pylatam

RUN python manage.py compilemessages -l es --settings=pylatam2024.settings && \
    python manage.py compilemessages -l en --settings=pylatam2024.settings && \
    python manage.py collectstatic  --noinput --settings=pylatam2024.settings

ADD docker/entrypoint.sh /run/
RUN chown -R pylatam:pylatam /run/ && \
    chmod +x /run/entrypoint.sh &&\
    chmod +x /run/launcher.sh &&\
    sed -i 's/proxy_set_header X-Forwarded-Proto $scheme;/proxy_set_header X-Forwarded-Proto https;/g' /etc/nginx/proxy_params

EXPOSE 80

CMD ["/run/entrypoint.sh"]
