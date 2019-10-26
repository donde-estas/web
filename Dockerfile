# Build static files (name as static for easier refference)
FROM node:alpine as static
RUN mkdir /app
WORKDIR /app
COPY ./package.json ./webpack.config.js /app/
RUN npm install --save-dev
ADD static /app/static/
RUN npm run build


# Python app package stage (build)
FROM python:3.8.0-alpine as final

RUN apk update \
  && apk add \
    bash \
    curl \
    build-base \
    postgresql-dev \
    postgresql-client \
    libpq \
    tzdata

WORKDIR /app
ADD requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD ./ /app

COPY dondeestas/local_settings.py /app/dondeestas/local_settings.py

# Copy static files generated in the static stage
# to the app container
COPY --from=static /app/static/webpack_bundles /app/static/webpack_bundles

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
