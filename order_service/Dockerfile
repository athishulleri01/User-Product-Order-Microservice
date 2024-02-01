# user_service/Dockerfile
FROM python:3.8

WORKDIR /app/order_service 

# Copy the entire content of the email_service directory to the working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
