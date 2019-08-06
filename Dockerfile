# Base Alpine Image
FROM python:3.7.2-alpine

# Update dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# Set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Add app
COPY . /usr/src/app

# Install dependencies
RUN pip install -r requirements.txt

# Add entrypoint
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Run app
CMD ["/usr/src/app/entrypoint.sh"]
