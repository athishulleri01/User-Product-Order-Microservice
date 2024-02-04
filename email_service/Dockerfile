FROM python:3.8
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /email_service  
# Copy the entire content of the email_service directory to the working directory
COPY . .

COPY migrate.sh /email_service/migrate.sh
COPY entrypoint.sh /email_service/entrypoint.sh

RUN chmod +x /email_service/migrate.sh
RUN chmod +x /email_service/entrypoint.sh

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# ENV DJANGO_SETTINGS_MODULE=email_service.settings

# Run app.py when the container launches
CMD ["sh", "./entrypoint.sh"]