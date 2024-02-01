FROM python:3.8

WORKDIR /app/product_service  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Copy the entire content of the email_service directory to the working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt