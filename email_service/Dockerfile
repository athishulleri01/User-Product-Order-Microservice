# # user_service/Dockerfile
# FROM python:3.8

# WORKDIR /app

# # Copy the entire content of the user_service directory to the working directory
# COPY ./email_service/ .


# user_service/Dockerfile
# email_service/Dockerfile
# email_service/Dockerfile
FROM python:3.8

WORKDIR /app/email_service  # Set the working directory to the email_service directory

# Copy the entire content of the email_service directory to the working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary port (if needed)
# EXPOSE 8001

# # Set the command to run your application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
