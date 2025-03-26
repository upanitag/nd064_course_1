# Use the official Python image as a base
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY project/techtrends/ /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 3111 to the outside world
EXPOSE 3111

# Command to run on container start
CMD ["sh", "-c", "python init_db.py && python app.py"]
