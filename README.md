# Celery example on Heroku

To follow this, you must have a heroku account. You must also have the heroku CLI installed. Follow these instructions to [get set up with Heroku and Python](https://devcenter.heroku.com/articles/getting-started-with-python)


You can run Celery locally (for testing purposes), but it's a little bit complicated because you have to run a number of processes in different windows of your terminal. If you want to see that (or try it) [here's a pretty clear example](https://www.youtube.com/watch?v=THxCy-6EnQM)


After you clone this repo, here are the basic steps you need to do:

0. Log into Heroku
```
heroku login
```

1. Create a new Heroku project for this 
```
heroku create 
```

2. Rename it if you like
```
heroku apps:rename celery-example
```
If that gives you errors, try  
```
heroku apps:rename celery-example --app old-app-name
```

3. Add your secrets and keys to tasks.py
* twilio account info
* twilio phone number
* your phone number (number for the app to text for testing purposes) 

3. Add cloudAMPQ to your celery-example Heroku project from the dashboard. Get its URL and paste that in the broker placeholder. You may have to put in a credit card number to verify that you're a real person (not a bot), but it is free at this tier. You won't be charged (unless you scale up... they will warn you if you accidentally do that.)

4. git commit it
```
git commit -am "commit your changes"
```

5. Push it to Heroku
Connect your git directory to the Heroku project
```
heroku git:remote -a my_app_name
```

```
git push heroku main
```

(or whatever the name of your git branch is. It might be master instead of main)

6. (You probably don't need to do this) If you edited the code and included any more packages, add that to the requirements.txt file with this command.
```
pip freeze > requirements.txt
```

7. (optional) Look at the logs to make sure Celery is running (and not crashing). BUT your app will probably not actually text you yet because you haven't given it enough processes to do the work yet.
```
heroku logs --tail
```

8. Create a two new process for celery: one for the worker and one for the beat. Type these at the terminal one at a time.
```
heroku ps:scale worker=1
heroku ps:scale beat=1
```

9. Look at the logs
```
heroku logs --tail
```

10. Check you phone. Got any texts?

11. When done, shut down the celery processes. Type these at the terminal one at a time.
```
heroku ps:scale worker=0
heroku ps:scale beat=0
```
