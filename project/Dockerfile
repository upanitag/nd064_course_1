FROM python:3.8
RUN ls -la 
COPY techtrends/ /app/

WORKDIR /app
RUN ls -l
RUN pip install -r requirements.txt

# Expose port 3111
EXPOSE 3111

#Command to run on container start
CMD ["python","init_db.py"]
CMD ["python", "app.py"]
