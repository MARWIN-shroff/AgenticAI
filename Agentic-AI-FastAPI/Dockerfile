# Use a lightweight Python image
FROM python:3.13.1

# Set the working directory
WORKDIR /app

# Copy requirements.txt before copying the entire app
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Command to start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



