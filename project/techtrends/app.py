import sqlite3

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort
import logging,sys

# Global variable to keep track of the connection count
connection_count = 0
# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    #Increment the global connection count after each connection.
    global connection_count
    connection_count = connection_count + 1
    return connection

def get_total_db_connections():
    return connection_count


def get_total_post_count():
    #Connect to the db
    connection = sqlite3.connect('database.db')
    global connection_count
    connection_count = connection_count + 1;
    total_posts=connection.execute('SELECT COUNT(*) FROM posts').fetchone()[0]
    #global connection_count
    #connection_count = connection_count - 1
    connection.close();
    return total_posts

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    if post :
        post_id, created, title, content = post
        app.logger.debug("Article " + title + " retrieved!")
        connection.close()
        #Decrease the count when closing the connection
        #global connection_count
        #connection_count = connection_count -1
        return post

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    #global connection_count
    #connection_count = connection_count -1 
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
      app.logger.error("Article " + str(post_id) + " doesn't exist")
      return render_template('404.html'), 404
    else:
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    app.logger.debug("About Us page is retrieved")
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            app.logger.info("Article " + title + " created" )
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()
            #global connection_count
            #connection_count = connection_count -1

            return redirect(url_for('index'))

    return render_template('create.html')

# Define the healthcheck endpoint functionality
@app.route('/healthz')
def health():
    # Create a response 
    response = { "result":"OK -health"}
    return jsonify(response),200

# Define metrics endpoint
@app.route('/metrics')
def metric():
    # Get the total number of database connections and total number of posts.
    response = {"db_connection_count": get_total_db_connections(), "post_count": get_total_post_count()}
    #response = {"db_connection_count": get_total_db_connections()}
    return jsonify(response),200
    
# start the application on port 3111
if __name__ == "__main__":
     #logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:app:%(asctime)s, %(message)s', datefmt='%d/%m/%Y, %H:%M:%S', handlers=[logging.StreamHandler(sys.stdout), logging.StreamHandler(sys.stderr)])
     logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:app:%(asctime)s, %(message)s', datefmt='%d/%m/%Y, %H:%M:%S', handlers=[logging.StreamHandler(sys.stdout)])
     app.run(host='0.0.0.0', port='3111')
