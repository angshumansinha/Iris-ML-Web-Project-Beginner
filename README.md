# Iris-ML-Web-Project-Beginner
A basic introduction to how to integrate ml with web development. <br>
The web app takes input and shows output in return<br>
For this we have used the well known IRIS dataset with parameters as Sepal length and Sepal Width and Petal length and Petal width<br>
SVC is used for prediction<br>
For the app, we have used Flask as backend<br>
![image](https://user-images.githubusercontent.com/68042268/120759707-ea9a1280-c530-11eb-8489-45cbd6d31d55.png)
So, sit and relax, grab some Popcorn and enjoy the coding experience
 ![image](https://user-images.githubusercontent.com/68042268/120759903-2503af80-c531-11eb-8546-730e7d8dd0f4.png)
<br>
<h1>#Happy Learning <3</h1><br><br>
 #A minimal Flask app : https://flask.palletsprojects.com/en/1.1.x/quickstart/
A Minimal Application<br>
A minimal Flask application looks something like this:<br>
<code>
from flask import Flask<br>
app = Flask(__name__)<br>
<br> <br>
@app.route('/')<br>
def hello_world():<br>
  return 'Hello, World!'</code><br>
So what did that code do?<br>
<ul>
 <li>First we imported the Flask class. An instance of this class will be our WSGI application.</li>

<li>Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.</li>

 <li>We then use the route() decorator to tell Flask what URL should trigger our function.</li>

<li>The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser</li>
 </ul>
 #App Screenshot<br>
 ![image](https://user-images.githubusercontent.com/68042268/120824048-ad0ba880-c575-11eb-9a52-92b7b960327b.png)<br>
 ![image](https://user-images.githubusercontent.com/68042268/120824139-c4e32c80-c575-11eb-98f8-1f79c63cc32e.png)


