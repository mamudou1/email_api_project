# Use slim Python 3.10 image as the base
FROM python:3.10-slim                        

# Set working directory inside the container to /app
WORKDIR /app                                 

# Copy requirements.txt to the working directory
COPY requirements.txt .       

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the app directory into the container
COPY ./app ./app                             

# Copy the .env file into the container (optional, won't fail if missing)
COPY .env* .                                  

# Start the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
