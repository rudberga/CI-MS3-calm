<h1 align="center">Calm</h1> 

![Mockup devices](https://github.com/rudberga/CI-MS3-calm/blob/master/static/img/mockups.png?raw=true "Mockup devices")


<p align="center"><strong>Milestone 3 project - Full Stack Web Developer course - Code Institute</strong></p>

This website is developed for users who wants to find artists who makes calm music. Maybe you need it for a rainy day, when you have to focus on studying or just to fall asleep in the evening. For any reason there is, this website will help the user to find new artists and contribute by adding their own. It is based on user contributions and you will be able to read others artist cards as well as add, delete and edit your own posts.

[Link to deployed website!](https://calm-music-project.herokuapp.com/) (UNDER MAINTENANCE!)

 
## UX

### User Stories

See below user stories:

> *- "As a user of the website, I expect to find a layout which is user friendly, so I easily can navigate throughout the website"*

> *- "As a user of the website, I expect to be able to register an account, so I can add, edit and delete my own artists"*

> *- "As a first time visitor of the website, I expect to be able to see artists without having to register, so I can get an idea of how the website works"*

> *- "As a user of the website, I expect to have all my own posts gathered on my profile page, so I easily can get an overview of my contributions"*

> *- "As a user of the website, I expect to be able to sign up for a newsletter, so I can get updates straigh to my inbox"*

> *- "As a user of the website, I expect to have easy access to social links, so I can check and possibly follow the social accounts"*

> *- "As a user of the website, I expect to get basic information and a link to the artist in the artist cards, so I can be informed before clicking the link"*

### Strategy

The main goal of this website is to create a sort of hub where users can come to find new artist they have not heard about, and also contribute with their own. The focus is on calm music so the users can trust that they will only get those recommendations. Users will be able to check artist without creating an account, however, in order to add their own artists they need to create an account.

Project goals: 

- Design a website which not only is user friendly and modern, but also brings a sense of calm by the design choices
- Present an inspiring page with artists cards where relevant info about the artist is included
- Present a smooth way for the user to add, edit and delete their contributions
- Give the user a simple way of registering, logging in and logging out

### Scope

The features of this website will let the users:

- Find artists through the artist page
- Search for artist in the search bar based on name, genre or nationality
- Register your own account so you can log in and contribute to the website
- Add artists for suggestion to other users, edit and delete them as well
- Include direct links to Spotify for easier navigation to listen to the artist

### Structure

The design and layout of this website will focus on the word 'calm'. Therefore picking up both the color theme and details such as rounded corners on all buttons, to remove elements that might pose as 'harsh'. The word 'calm' also made me focus on using modals to create a smoother experience for the user, not having to see a new rendered page for each button they press.

### Skeleton

[Wireframe](static/docs/ci-ms3-calm.pdf)

6 pages included in the wireframe which are:
- Landing Page
- Login Modal
- Register Modal
- Artist Page
- Add Artist Module
- Profile Page

### Surface

#### Main inspiration
 
I took my main inspiration from the world 'calm' and what I associate with it, also what I believe other people associate with it. What I came up with was to base the design out of the color blue and feeling of a forrest with a lake. The shade of blue comes together with a green tone to give the calming appearance of the website. Nothing screams out in terms of color or shape.

#### Fonts

For the fonts in this project I decided to play with the font weights of the font 'Barlow'. I think this font fits my website as it is not too aggressive in its approach and it looks modern.

#### Barlow weight 400

This is the font weight used for standard text such as inside the artist cards

![Barlow](https://github.com/rudberga/CI-MS3-calm/blob/master/static/img/barlow-400.png?raw=true "Barlow 400 weight")

#### Barlow weight 700

This is the font weight used for the bigger texts such as on the landing page

![Barlow](https://github.com/rudberga/CI-MS3-calm/blob/master/static/img/barlow-700.png?raw=true "Barlow 700 weight")

#### Colors

The color theme I have decided to go with focuses mainly on blue with green hints.

I have therefore focused on below colors:

- #d0e8f2
- #79a3b1
- #456268

![Colors](https://github.com/rudberga/CI-MS3-calm/blob/master/static/img/color-palette.png?raw=true "Color Palette")

## Features

 
### Existing Features

- **Social links**: in the footer you will find the icons for Inspiry's different social platforms
- **User Account**: create your own user account with username and password
- **Login/Logout**: functionality that let you log in and log out in a simple way
- **Add, Edit, Delete Artists**: functionality that let you add, edit and delete your own contributions
- **Direct Link**: every artist card has a direct link to Spotify (via icon) in order for the user to easier access the artist
- **Artist page**: where the user can see all contributions from all users and click on each artist for more information
- **Profile page**: users own profile page where they will see all of their own contributions
- **Search**: search function on the artist page where the user can search for artists based on name, nationality or genre
- **Newsletter**: users can register for a newsletter list when they are logged in

### Features Left to Implement

- **Favorite list**: let every user add their favorite artists to their own profile
- **Carousel**: with the most favorited artists

## Technologies Used 

**Languages / Markup** 

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - Markup language

- [CSS](https://en.wikipedia.org/wiki/CSS)
    - Main programming language
    
- [Python](https://www.python.org/)
    - Main programming language
    
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - Main programming language
    
**Database**

- [MongoDB](https://www.mongodb.com/)
    - Document based data framework to store the applications data

**Frameworks**

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - Framework used with python to create the application. Imported via app.py

- [Materialize](https://materializecss.com/)
    - Framework used in order to improve the structure and design of the website. Imported via CDN

- [jQuery](https://jquery.com/)
    - Framework used with JavaScript in order to simplify the code. Imported via CDN

**Version control**

- [GitHub](https://github.com/)
    - Used for version control of the project
    
**Cloud platform**

- [Heroku](https://heroku.com/)
    - Used for deploying and running application

**Other**

- [Gitpod](https://gitpod.io/)
   - IDE which was used for the project. Directly linked to repository through GitHub

- [Google Fonts](https://fonts.google.com/)
   - Used for all the fonts in the project. Connected to CSS via @import
   
- [Font Awesome](https://fontawesome.com/)
   - Used for all the icons in the project. Connected to HTML via CDN

- [Unsplash](https://unsplash.com/)
   - Used for images in the project. Imported locally through assets/img

- [Canva](https://www.canva.com/)
   - Used for making main icon. Imported locally through assets/img

- [Jinja](http://jinja.palletsprojects.com/)
   - Templating language used in this app
   

## Testing 

I have done a lot of testing throughout the project and below you will find it in a more structured manner. I have made sure that the user stories are tested and works well, also focused on responsiveness where I have used resources online as well as the physical devices I had access to. Whenever a new functionality of the site was implemented, I tested it. At the end of the development journey, I had a big testing day where I went through the sites full functionality again.

### Tests done in order to secure UI components

| Test | Method | Expected | Result |
| ---- | ------ | -------- | ------ |
| Log In | ------ | -------- | ------ |
| Buttons 1 - Log In| Entered website and landed on index.html, pressed button 'Login' | Modal to pop up with form to log in | PASS - result as expected |
| Buttons 2 - Log In| Inside modal for login press button 'Log In' without filling in anything | Info should pop up telling user that they need to fill in username | PASS - result as expected |
| Buttons 3 - Log In| Inside modal for login press button 'Log In' only filling in username | Info should pop up telling user that they need to fill in password | PASS - result as expected |
| Buttons 4 - Log In| Inside modal for login press button 'Log In' filling in incorrect username and password then press 'Log In' | Alert box should come up telling user either password or username are wrong | PASS - result as expected |
| Buttons 5 - Log In| Inside modal for login press button 'Log In' filling in correct username but wrong password then press 'Log In' | Alert box should come up telling user either password or username are wrong | PASS - result as expected |
| Buttons 6 - Log In| Inside modal for login press button 'Log In' filling in a correct password but wrong username then press 'Log In' | Alert box should come up telling user either password or username are wrong | PASS - result as expected |
| Buttons 7 - Log In| Inside modal for login press button 'Log In' filling in a correct username and password then press 'Log In' | User should be redirected to the Artist-page | PASS - result as expected |
| Sign Up | ------ | -------- | ------ |
| Buttons 1 - Sign Up| Entered website and landed on index.html, pressed button 'Sign Up' | Modal to pop up with form to register new user | PASS - result as expected |
| Buttons 2 - Sign Up | Inside modal for sign up press button 'Sign Up!' without filling in anything | Info should pop up telling user that they need to fill in username | PASS - result as expected |
| Buttons 3 - Sign Up | Inside modal for sign up press button 'Sign Up!' when only filling in username | Info should pop up telling user that they need to fill in password | PASS - result as expected |
| Buttons 4 - Sign Up | Inside modal for sign up press button 'Sign Up!' when only filling in password | Info should pop up telling user that they need to fill in username | PASS - result as expected |
| Buttons 5 - Sign Up | Inside modal for sign up press button 'Sign Up!' when only filling in password | Info should pop up telling user that they need to fill in username | PASS - result as expected |
| Buttons 6 - Sign Up | Inside modal for sign up press button 'Sign Up!' when only checking box for terms | Info should pop up telling user that they need to fill in username | PASS - result as expected |
| Buttons 7 - Sign Up | Inside modal for sign up press button 'Sign Up!' when only filling in username and password | Info should pop up telling user that they need to tick checkbox | PASS - result as expected|
| Buttons 8 - Sign Up | Inside modal for sign up press button 'Sign Up!' when only filling in either username and password and ticking the box | Info should pop up telling user that they need to fill in the field that is empy | PASS - result as expected |
| Buttons 9 - Sign Up | Inside modal for sign up press button 'Sign Up!' when filling in a username that already exists | Info should pop up telling user that the username already exists | PASS - result as expected |
| Buttons 10 - Sign Up | Inside modal for sign up press button 'Sign Up!' when filling in all new information and ticking checkbox | User should be redirected to profile page | PASS - result as expected |
| Navbar | ------ | -------- | ------ |
| Buttons 1 - Navbar | Entered website and landed on index.html, pressed navbar button 'Login' | Modal for log in should pop up | PASS - result as expected |
| Buttons 2 - Navbar | Entered website and landed on index.html, pressed navbar button 'Sign Up' | Modal for signing up should pop up | PASS - result as expected |
| Buttons 3 - Navbar | Entered website and landed on index.html, pressed navbar button 'Artists' | User should be redirected to artists page | PASS - result as expected |
| Buttons 4 - Navbar | Entered website and landed on index.html, logged in, pressed navbar button 'Profile' | User should be redirected to profile page | PASS - result as expected |
| Buttons 5 - Navbar | Entered website and landed on index.html, logged in, pressed navbar button 'Logout' | User should be redirected to index page and logged out | PASS - result as expected |
| Buttons 6 - Navbar | Navbar further tested to go back from each page | User should be redirected to page that the button says | PASS - result as expected |
| Newsletter | ------ | -------- | ------ |
| Buttons 1 - Newsletter | Clicked logo 'Calm' when logged in | User should be redirected to the index page with newsletter form | PASS - result as expected |
| Buttons 2 - Newsletter | Clicked 'Submit' without filling in anything | Info should pop up telling user that they need to fill in the email | PASS - result as expected |
| Buttons 3 - Newsletter | Clicked 'Submit' when filling in an e-mail with wrong format | Info should pop up telling user that they need to fill in correct format | PASS - result as expected |
| Buttons 4 - Newsletter | Clicked 'Submit' when filling in an e-mail correctly | Alert box should pop up saying they are subscribed | PASS - result as expected |
| Buttons 5 - Newsletter | Clicked 'Submit' when filling in an e-mail that already exists | Alert box should pop up saying they are already subscribed | PASS - result as expected |
| Artist page | ------ | -------- | ------ |
| Buttons 1 - Artist page | Clicked on the artist card image | Information about artist should come up | PASS - result as expected |
| Buttons 2 - Artist page | Clicked on pen button on artist card | Redirect to edit artist page | PASS - result as expected |
| Buttons 3 - Artist page | Clicked on trash can button | Warning should pop up asking user if they want to delete | PASS - result as expected |
| Buttons 4 - Artist page | Clicked on plus button | Add artist modal should pop up | PASS - result as expected |
| Buttons 5 - Artist page | Filled in search field and clicked on search icon | Search result should appear | PASS - result as expected |
| Buttons 6 - Artist page | Left search field empty and clicked on search icon | No results should appear | PASS - result as expected |
| Buttons 5 - Artist page | Filled in search field, clicked search and then the reset | Should empty search field and reset artist page | PASS - result as expected |
| Social Links | ------ | -------- | ------ |
| Buttons 1 - Social links| Clicked on each button for social links | Redirect to social links page on new tab | PASS - result as expected |

### Tests done in order to secure structural integrity

#### Modals

Each modal implemented on the website was tested on several screen sizes and confirmed that it kept its responsive design.

This includes the modals for:

- Log in
- Sign up
- Add artist

#### Fonts

Fonts are consistent throughout the website, this was checked by simply controlling each part of the website with chrome dev tools.

### Testing forms + Post & Get to/from DB

As the website rely heavily on its forms for both user authentication as well as adding and editing artist cards, extensive testing on them was made. 

#### Login 
Tested by:
- entering correct login info and logging in, got the data correctly from DB everytime
- entering incorrect login info and trying to login
- entering nothing and trying to login

#### Sign Up
Tested by:
- entering new user information and click sign up, posted the information correctly to DB everytime
- entering already existing user information, got the already registered user information everytime
- entering nothing and trying to sign up


#### Add Artist 
Tested by:
- entering new artist information and click add, posted the information correctly to DB everytime
- entering already existing artist information, function for get in this case is still under development
- tested leaving fields empty to see that it did not work to add

#### Edit Artist 
Tested by:
- changing one field and click add, updated the data in DB everytime
- changing fields and click cancel, did not change anything

### Bugs

| Bug | Solution | Current status |
| --- | -------- | -------------- |
| Connection to MongoDB stopped working after changing geolocation from Japan to Sweden | Solved by creating a new cluster with the server based in Germany instead of Singapore | Solved |
| When searching for an artist the error message "pymongo.errors.OperationFailure" shows up | Solved by creating a new search index via the CLI which was missed when creating a new cluster | Solved |
| Logo does not show on profile page | Solved by adding a "url_for" in order to get the picture instead of a direct path | Solved |
| Genre dropdown in modal for add artist does not generate any options | Solved by adding a get method to get genres from db in the "get_artist" function | Solved |
| Login forms fields are difficult to mark and fill in | Solved by adding "pointer-events: none" directly to html | Solved |
| Styling of alert box disappeared | Solved by moving the style class to the correct div | Solved |


### Browser and screen size responsiveness testing

Have done extensive testing in Chrome DevTools, different browsers as well as on physical devices I had access to. The website is responsive and it acts as it is supposed to when changing between devices, browsers and screen sizes.

**Websites used for testing on different screen sizes (other than what is mentioned above):**

- [whatismyscreenresolution.net](http://whatismyscreenresolution.net/multi-screen-test)
- [responsivetesttool.com](http://responsivetesttool.com/)

### HTML Validator (W3C Markup) - [Link](https://validator.w3.org)

Pushed my HTML code through the validator and got following messages which I corrected:

| Message | Solution |
| ------- | -------- |
| Attribute a not allowed on element a at this point | Solved by removing one "a" in the tag as it accidentally was two of them |
| Character reference was not terminated by a semicolon | Solved by adding ";" to the end of the emojis |
| An img element must have an alt attribute, except under certain conditions. | Solved by adding alt that was missing |

**IMPORTANT!** Because I am using the jinja templating language in this app, there is bound to show a lot of warnings and errors connected to that. These warnings and errors have been checked and controlled and are deemed to be safe to disregard as they are not true errors for the application.

### CSS Validator (W3C CSS) - [Link](https://jigsaw.w3.org/css-validator)

Pushed my CSS code through the validator and got following messages which I corrected:

| Message | Solution |
| ------- | -------- |
| Value Error background-color 'none' is not a background-color value 'none' | Solved by adding 'transparent' instead of 'none' |

Also received a few warnings including for the variables created in CSS, I decide to disregard these warnings as I am confident that they do not pose any error for the website.

### JSHint - [Link](https://jshint.com/)

Pushed my JavaScript code through JSHint where no major issues showed up.

| Message | Solution |
| ------- | -------- |
| No relevant warnings and no errors showing. | - |

The report shows that there are several undefined variables '$', this is caused by using jQuery and therefore we can disregard them.

### PEP8 - [Link](http://pep8online.com/)

Pushed my Python code through PEP8 where only a few minor issues showed up, such as whitespace where it should not be. Everything is now solved and it does not show any issues anymore. 

| Message | Solution |
| ------- | -------- |
| No relevant warnings and no errors showing. | - |

### User stories result

All of the testing and debugging above have left us with the result below on achieving the goal of our user stories listed in the top of this readme:

| User story | Result |
| ---------- | ------ |
| User friendly layout | PASS |
| Register account, add, edit & delete artists | PASS |
| Preview of artists before signing up | PASS |
| Users posts gathered on profile page | PASS |
| Newsletter | PASS |
| Access to social links | PASS |
| Information about each artist | PASS |

## Deployment

In order to deploy my website I used Heroku. The deployment was made from the master branch and I did it through below steps:

 1. Firstly, we need to create a .txt file which will contain the project dependencies. Open the project in Gitpod, in the CLI run: 

 `pip3 freeze --local > requirements.txt`

 2. In Gitpod, create a file named "Procfile". Inside this file you will have to enter: 
 
 `web: python app.py`
 
 This is for Heroku to know which language the application will be running on.
 
 3. After these two steps you need to commit to Github, this is very important, otherwise Heroku will not be able to deploy the project.
 
 4. Enter the Heroku website [https://www.heroku.com](https://www.heroku.com/), sign in with your log in credentials
 
 5. Click button "New" on the dashboard and select "Create new app".

 6. Enter an unique name of your application -> select your region -> click "Create App".
 
 7. Back on the applications dashboard in Heroku, select "Settings".
 
 8. Copy the Heroku git URL under the "App Information".
 
 9. Go back to Gitpod and into the CLI run 
 
   `git remote add heroku "Paste your Heroku Git URL here"`
 
 10. Still in the CLI, run 
 
   `heroku ps:scale web=1`
   
 11. Enter the MongoDB website [https://www.mongodb.com](https://www.mongodb.com), sign in with your log in credentials
 
 12. When logged in and on your dashboard, select the cluster of your database and click "Connect".
 
 13. Click "Connect your application" among the options that appear.
 
 15. Choose Python as your driver and the version that you have.
 
 14. Copy the field under "Add your connection string into your application code".

 15. Go back to the Heroku website and your applications dashboard -> Click "Settings" -> Click "Reveal Config Vars".
 
 16. Click "Add" and enter the information below:

`IP` : `0.0.0.0`

`PORT`: `5000`

`MONGO_URI` : `PASTE THE CONNECTION STRING COPIED FROM MONGODB`

- IMPORTANT! Inside the connection string, replace `<password>`with your MongoDB Database access password
- IMPORTANT! Inside the connection string, replace `test` with the name of the database of your project

`SECRET_KEY` : `secret key you have entered in env.py file`

17. Click "More" in the top right corner -> Click "Restart all dynos" and confirm

18. The app is now deployed and you can open it via the button "Open App"

### Running my project locally

In order to run the project locally you should firstly enter my repository by the link https://github.com/rudberga/CI-MS3-calm.
 
1. Click the button **Code**
2. Choose either **HTTPS**, **SSH** or **GitHub CLI**, then click the copy icon to the right of the link
3. You will then open the terminal in your IDE
4. Type `git clone` and then paste the URL you copied
5. Press **Enter** and you will have created a local clone in your IDE

You could also have it open directly in Gitpod if you are using it, see below:

1. Open the repository https://github.com/rudberga/CI-MS3-calm
2. Click the green **Gitpod** button 
3. Gitpod will now open up a new workspace with the code from this project

After these basic steps you will have to take further steps in order to make your IDE run the project. This is mainly instructions for Gitpod as that is the IDE that I was using. The steps might have to be adjusted depending on the IDE you use.

1. To be able to run the application, you will have to create a .txt file with all the dependencies. To do this you can simply run below command in the CLI:

`pip3 install -r requirements.txt`

2. Create a "env.py" file, which you should add to your .gitignore as it will contain security information.

3. In order to run this project locally you will have to create a matching DB in Mongo DB.
 
4. Create a new database called "calm" with the collections: 
- "genres" 
- "artists"
- "users"
- "newsletters"

5. Choose Python as your driver and the version that you have.
 
6. Copy the field under "Add your connection string into your application code".

7. Open your env.py in your IDE and enter this information in this order from top to bottom:

`import os`

`os.environ.setdefault("IP", "0.0.0.0")`

`os.environ.setdefault("PORT", "5000")`

`os.environ.setdefault("SECRET_KEY", "replace this with your own secret key")`

`os.environ.setdefault("MONGO_URI","your mongo URI copied in step 6, replace < password > with your MongoDB Database access password. replace < test > with the name of the database of your project")`

`os.environ.setdefault("MONGO_DBNAME", "calm")`

8. Save the file and it should be ready to run locally.

## Credits

### Content

- The text on all the pages of the website was written by myself

### Media
- Images on this website was imported from [Unsplash](https://unsplash.com/)
- Logo for this website made by myself through the editor in [Canva](https://www.canva.com/)

### Code

I have modified these code snippets in order for them to work in my project.
- Hovering over social links and icons: [Ian Lunn](https://ianlunn.github.io/Hover/#effects)
- Alert boxes: [pradeep1616](https://codepen.io/pradeep1616/pen/LxaRRB)
- Partly covered backgrounds: [CSS Tricks](https://css-tricks.com/forums/topic/css-background-with-2-colors)
                             & [G-Cyrillus](https://stackoverflow.com/questions/38398434/half-image-half-color-responsive-background)
- Capitalize first letter in jinja template: [Shubham Jain](https://shubhamjain.co/til/capitalizing-first-letter-in-jinja)

### Disclaimer

This is a project for the course Full Stack Web Development diploma with Code Institute, it is not for commercial use. If you find any of your content that you want removed, please contact me directly via my e-mail rudberg@pm.me.
