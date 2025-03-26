FROM python:3.8

COPY techtrends/init_db.py /app/
COPY techtrends/app.py /app/
COPY techtrends/requirements.txt /app/
COPY techtrends/schema.sql /app/
COPY techtrends/database.db /app/
COPY techtrends/static/css/main.css /app/static/css/
COPY techtrends/templates/*.html /app/templates/
WORKDIR /app
RUN ls -l
RUN pip install -r requirements.txt

# Expose port 3111
EXPOSE 3111

#Command to run on container start
CMD ["python","init_db.py"]
CMD ["python", "app.py"]
