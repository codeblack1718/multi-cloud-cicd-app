# Use a lightweight version of Python
FROM python:3.9-slim

# Set the working folder inside the container
WORKDIR /app

# Copy the files into the container
COPY . .

# Install required Python packages
RUN pip install -r requirements.txt

# Tell the container how to start your app
CMD ["python", "app.py"]
