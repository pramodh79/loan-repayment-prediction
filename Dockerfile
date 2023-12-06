# Use a base image with the necessary dependencies
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model files into the container
COPY . /model

# Copy the rest of the application files
COPY . /app

# Set environment variables
ENV MODEL_PATH /model/loan_prediction_model.h5
ENV FLASK_APP /app/app.py

# Expose the necessary port
EXPOSE 5000


# Command to run your application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]


