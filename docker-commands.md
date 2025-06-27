1. Build the Docker Image
Open your terminal in the project root (where the Dockerfile is located) and run:

docker build -t email_api_project .

2. Run the Docker Container
This maps port 8000 on your machine to port 8000 in the container.

docker run -d -p 8000:8000 --name email_api_container email_api_project

3. Test the API
Open your browser or use curl/Postman to access:

