FROM python:3.8

COPY . /app
WORKDIR /app
RUN pip install -r project/techtrends/requirements.txt

# Expose port 3111
EXPOSE 3111

#Command to run on container start
CMD ["python","init_db.py"]
CMD ["python", "app.py"]
