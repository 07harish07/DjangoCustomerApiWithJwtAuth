From python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc postgresql-dev libffi-dev libc-dev linux-headers

RUN pip install -r requirements.txt

RUN apk del .tmp

RUN mkdir /app
COPY ./CustomerAPI /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web

RUN adduser -D user
RUN chown -R user:user /vol

RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]