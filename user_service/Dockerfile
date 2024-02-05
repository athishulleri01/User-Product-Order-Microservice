FROM python:3.8

WORKDIR /app/product_service  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Copy the entire content of the email_service directory to the working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# FROM python:3.8

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /app/user_service

# # Install system dependencies
# RUN apt-get update && apt-get install -y libpq-dev gcc

# # Copy only the requirements file to leverage Docker cache
# COPY requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the entire project
# COPY . .

# COPY entrypoint.sh /app/user_service/entrypoint.sh
# RUN chmod +x /app/user_service/entrypoint.sh

# ENV DJANGO_SETTINGS_MODULE=miniproject.settings

# EXPOSE 8000

# # Run entrypoint.sh when the container launches
# CMD ["sh", "./entrypoint.sh"]
