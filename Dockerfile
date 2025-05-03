FROM python:3.13-alpine

# Setup
RUN mkdir /app
COPY pip_packages.txt /
RUN pip install --no-cache-dir -r /pip_packages.txt

# Copy files over
COPY bin /app/bin
COPY gunicorn.conf.py /app
COPY app.py /app

# Run as different user
RUN addgroup -S discord && adduser -S discord -G discord
USER discord

# Start app
WORKDIR /app
CMD ["python", "/app/app.py"]
