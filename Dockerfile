# Base Alpine Image
FROM python:3.7.1-alpine

# Set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Add app
COPY . /usr/src/app

# Install dependencies
RUN pip install -r requirements.txt

# Run app
CMD python manage.py run -h 0.0.0.0
