# # user_service/Dockerfile
# FROM python:3.8

# WORKDIR /app

# # Copy the entire content of the user_service directory to the working directory
# COPY ./user_service/ .

# # Explicitly copy requirements.txt to the working directory
# COPY ./requirements.txt .

# RUN pip install -r requirements.txt
# user_service/Dockerfile
FROM python:3.8

WORKDIR /app/user_service 
# Copy the entire content of the email_service directory to the working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
