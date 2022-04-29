# The Jungle

## Index
- [Project Description](#project-description)
- [Technologies](#technologies-used)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Project Description

- The Jungle is a social media web application inspired by other existing successful social media platforms.
- The Jungle allows people to interact with friends, family, and others who have similar interests.
- Users are able to create accounts, login, search for other users, create posts, react to a post, make comments, create/join groups, and use chatrooms.
- Detailed description of features can be found [here](#features) 

## Technologies Used

* Backend
   * PostgreSQL - 42.3.1
   * Java - 17.0.1
      * TestNG - 7.4.0
      * Javalin - 4.1.1
      * Cucumber - 7.1.0
      * Selenium - 4.1.1
      * Mockito - 0.4.13
      * Gson - 2.8.9
      * log4j - 2.17.0
   * Python - 3.9
      * behave - 1.2.6
      * Selenium - 4.1.0
      * Flask - 2.0.2
      * Psycopg - 3.0.8
      * pytest - 6.2.5
        * MagicMock
* Frontend
   * HTML 5
   * CSS 3
   * Javascript
   * Bootstrap
   * Figma
* Other
   * Postman
   * DBeaver

## Features

### List of features ready and TODOs for future development
* Registration Feature
   * Users are able to register a new account using unique username and email
* Login Feature
   * Users are able to login using their username and password
* User Profile Feature
   * Users are able to write "About Me" in their profile for others to see
* Search Other Users Feature
   * Users are able to search other users using username 
* View Post Feed Feature
   * Users are able to view posts
* Post Feature
   * Users are able to make a post
* Comment Feature - UNFINISHED
   * Users are able to comment on a post
* Reaction Feature - UNFINISHED
   * Users are able to react to a post
* Group Feature
   * Users are able to create groups
   * Users are able to join groups
* Chatroom Feature
   * Users are able to join chatroom
   * Users will see previous chat history up to 5 minutes upon joining a chat
   * Types of chatroom
      * Global chatroom - All users can join
      * Group chatroom - Only users that are in the specific group can join

### To-do list:
* Follower/Following Feature
   * Users are able to follow and unfollow as well as view the number of followers and following
   * Users should only see posts from following users
* Upload Profile Picture Feature
   * Users are able to upload profile picture to stylize their profile
* Dark Mode Feature
   * Users are able to toggle dark / light theme depending on their preference
* Host/Join events Feature
   * Users are able to host new events
   * Ways to join
      * Join
      * Invitation
* Session Management Feature
   * The user's session is maintained until the user logs out
* Reset Password Feature
   * Users are able to reset their password
* Bookmark Posts Feature
   * Users are able to bookmark or save posts to save them in an archive
* Auto-remove Posts Option Feature
   * Users are able to set a time frame to automatically have their posts delete themselves after they are posted.
* Profanity filter Feature
   * Filtering profanity to ensure professional and friendly social media environment
* "See First" Option For Other Users Feature
   * Users are able to prioritize / favorite users to display their posts first before other users' posts

## Getting Started
   
```
// Currently as of Feb / 3 / 2022, the main branch contain several bugs that were fixed in hkim-ma branch.

git clone https://github.com/revature-The-Jungle/The-Jungle.git
git fetch
git checkout hkim-ma
```

```
Create a postgres RDS in amazon AWS

Download apache and Jenkins in AWS EC2

Download the S3 publisher plugin for Jenkins

Create 3 new freestyle protects. For JavaAPI, PythonAPI and FrontEnd.

Create the enviroment variables in Jenkins.

Configure webhooks in github.
```
```
For JavaAPI:

Add the path to the pom file

configure pom and add testng.xml file the repo.

Click git project and connect Jenkins to the git repo.

Execute the shell command in the build section:

java -jar JavaAPI/target/The-Jungle-1.0-SNAPSHOT.jar 
```
```
For PythonAPI:

Set up git repo connection.

Make sure to have all the dependencies installed in EC2

execute the shell command 

pytest <routes to the test files>
python3 PythonAPI/main.py
```
```
For FrontEnd:

Configure the git repo

In the post build section select publish artifacts to s3 bucket.

In the source section enter: FrontEnd/** 

Enter the destanation bucket and save.
```

## Usage

> Here, you instruct other people on how to use your project after they’ve installed it. This would also be a good place to include screenshots of your project in action.

## Contributors

- [Angel Arroyo](https://github.com/AArroyo021)
- [Adam Januszewski](https://github.com/AdamsCodeAndProjects)
- [Ahnaf Chowdhury](https://github.com/ahnaf717) 
- [Alejandro Lara](https://github.com/alara505)
- [Alejandro Fuste](https://github.com/Alejandro-Fuste)
- [Amanda Gonzalez](https://github.com/amandue10)
- [Christian Ayala](https://github.com/Chris24xx)
- [Daniel Landeros](https://github.com/Virtud87)
- [David Zazulak](https://github.com/dZazulak)
- [Dearce Goodman](https://github.com/DearceGoodman)
- [Eric Jennings](https://github.com/ericthered1138)
- [Hyungsuk Kim](https://github.com/hsKim93)
- [Irfan Uludag](https://github.com/Uirfan)
- [Kyla Karnoski](https://github.com/bluedragonscales)
- [Loc Phan](https://github.com/LocPhanRevature)
- [Mohammad Bahrami](https://github.com/mohbah)
- [Victor Flores Herrera](https://github.com/VictorFloresHerrera)
