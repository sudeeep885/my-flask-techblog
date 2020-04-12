# my-flask-techblog
This is a blog application made in Flask. Please visit the deployed version (refresh the page, if it shows internal error)
http://myflaskblog.pythonanywhere.com/

It includes the following functionalities :
1) User registration
2) User login
3) User can upload his/her profile picture
4) User can create / read / update / delete a blog post
5) User logout

Tables created in MYSQL DATABASE :
1) Users(id, profile_pic, email, username, hashed_password)
2) BlogPost(id, user_id, title, date, text)

# Steps to follow in order to run on you system : 
1) Create credentials.py file in root directory having secret_key and sqlalchemy_database_uri variable along with it's value as a string
2) Open command prompt and run
     <ol>
        <li>flask db init</li>
        <li>flask db migrate -m "first migration"</li>
        <li>flask db upgrade</li>
        <li>and then run the app by writing,   python app.py</li>
     </ol>
 
