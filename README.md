# Music Time Machine 

A program takes top 100 songs from which date you typed to console and create a Spotify playlist.

Through this project, you can create a popular songs playlist on Spotify according to which date you want. 


[Billboard](https://www.billboard.com/) compiles a list of the top 100 songs. So these are the most played songs during a particular week. And if you go to [The Hot 100](https://www.billboard.com/charts/hot-100/) section, you'll see it for the current week, but there's also a feature where you can change the date to any data in the past 20 years.

<p align="center">
  <img src="https://i.ibb.co/k5D0rky/flight-dealer.png" alt="flightdealer"/>
</p>

# Installing
Download the [Python 3](https://python.org) installer package from the official website and install it, if not installed previously.

* Run the following in the terminal to install the modules to run your program without excussions.
```
pip install bs4
```

```
pip install requests
```

```
pip install spotipy
```
# Authentication with Spotify

* In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one [here](http://spotify.com/signup/).
* Once you've signed up/ signed in, go to the [developer dashboard](https://developer.spotify.com/dashboard/) and create a new Spotify App:
*  Once you've created a Spotify app, copy the **Client ID** and **Client Secret** into your Python project.
* Spotify uses [OAuth](https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth) to allow third-party applications (e.g. our Python code) to access a Spotify user's account without giving them the username or password.


# How to Use?

Download the source code from the repository and run the file just as any other Python script (.py) file.
```
python3 main.py
```

* Note! For the code to work you need to replace all the placeholders with your own details. e.g. ```CLIENT_ID```, ```CLIENT_SECRET```.

Once you replace the own details in the code, run the program.

Then type which date you want to create a playlist on Spotify. If everything is okay, you should see the page below show up automatically (be sure to click Agree):

<p align="center">
  <img src="https://i.ibb.co/k5D0rky/flight-dealer.png" alt="flightdealer"/>
</p>

Then it will take you to the page below, example.com and you need to copy the entire URL in the address bar:

Check out the link below for more details about API sources.

# Description


# Documentations

* [Spotipy Documentation](https://spotipy.readthedocs.io/en/2.13.0/#)
* [Spotify Developer](https://developer.spotify.com/)
* [What the Heck is OAuth?](https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth)
* [Google Sheets](https://docs.google.com)
