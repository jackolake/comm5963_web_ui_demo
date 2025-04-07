FROM python:3.13.2-slim-bookworm

# Create app folder
WORKDIR /app
COPY . /app

# Install Python packages
RUN pip install -r requirements.txt

# Kick start our app with Gunicorn
CMD ["gunicorn", "--config", "gunicorn_config.py", "app:app"]