# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the bot files into the container
COPY . /app

# Install the bot dependencies
RUN pip install -r requirements.txt

# Run the bot
CMD ["python", "main.py"]
