FROM python:3.8

COPY project/techtrends/init_db.py /app/
COPY project/techtrends/app.py /app/
COPY project/techtrends/requirements.txt /app/
COPY project/techtrends/schema.sql /app/
COPY project/techtrends/database.db /app/
COPY project/techtrends/static/css/main.css /app/static/css/
COPY project/techtrends/templates/*.html /app/templates/
WORKDIR /app
RUN ls -l
RUN pip install -r requirements.txt

# Expose port 3111
EXPOSE 3111

#Command to run on container start
CMD ["python","init_db.py"]
CMD ["python", "app.py"]
