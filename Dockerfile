FROM python:3.10-slim                        
# Use slim Python 3.10 image as the base

WORKDIR /app                                 
# Set working directory inside the container to /app

COPY requirements.txt .                      
# Copy requirements.txt to the working directory
RUN pip install --no-cache-dir -r requirements.txt 
# Install Python dependencies

COPY ./app ./app                             
# Copy the app directory into the container
COPY .env .                                  
# Copy the .env file into the container

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] # Start the FastAPI
