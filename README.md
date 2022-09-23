# Astro Riders

Astro Riders is a football group designed in a way that users can manage and organise the members and Events. This site allows users to implement the CRUD operations.

A live website can be found [here](https://teamer-app.herokuapp.com/).

![website preview](static/wireframes/am%20i%20responsive.png)

<!-- TOC --><a name="table-of-contents"></a>
## Table of Contents
<!-- TOC start -->
- [Astro Riders](#Astro Riders)
  * [Table of Contents](#table-of-contents)
    + [User Experience](#user-experience)
    + [Project Goals](#project-goals)
    + [Scope](#scope)
      - [User Stories](#user-stories)
    + [Project Management](#project-management)
    + [Wireframe](#wireframe-1)
    + [Surface](#surface)
    + [Features](#features)
    + [Languages Used](#languages-used)
    + [Technology Used](#technology-used)
    + [Testing](#testing)
      - [Validation Testing:](#validation-testing)
    + [Bugs:](#bugs)
      - [Known Bugs:](#known-bugs)
    + [Deployment:](#deployment)
    + [Credits:](#credits)
    + [Acknowledgements](#acknowledgements)
<!-- TOC end -->
<br/>

# User Experience

### Project Goals
The goal of the project is to create a football group where players can add themselves by signing up where they can create an event and delete an event.

The personal goals for this website are:     
- The site is easy to navigate and user friendly.
- The purpose of the site is evident and inviting to users.
- That users want to signup and engage with its content. 

# Scope

According to the project, not all features can be implemented in the first release of the project.
For this reason, the project will be divided in multiple phases.The first phase will include the features that have been identified in order to build the minimum requirement.

First Phase

- Create a Signup page
- Create a Signin page
- Create Member Profile page
- Members list page

Second Phase

- Create Event page
- Delete Event page
- Events list page
- Member can add themselves to an Event
- Member can delete themselves from an Event

Third Phase

- Add playing position in member edit profile page.
- Success page for all event crud operations.


### User Stories
As a first time user I want to:

- Easily understand the main purpose of the site, so that I can easily use the site.
- Easily navigate through the site, so that I can easily find content and clearly see where I am on the site.
- Signup to the website, independently register and gain access to the website.
- Login into the website which allows a user to gain access to an application by entering their username and password.

As a registered member:

- As a registered member, I want to create an Event.
- As a registered member, I want to delete an Event.
- As a registered member, I want to add myself to an event.
- As a registered member, I want to remove myself from an event.
- As a registered member, I want to delete the game that I created.
- As a registered member, I want to edit my profile.

[Go to the top](#table-of-contents)

# Project Management

GitHub projects was used as a project management tool. Kanban board was used to add user stories and follow the project progress.

**Week 1**
![Project Management](static/kanban/kanban_week_1.png)

**Week 2**
![Project Management](static/kanban/kanban_week_2.png)

**Week 3**
![Project Management](static/kanban/kanban_week_3.png)

**week 4**
![Project Management](static/kanban/kanban_week_4.png)

**Week 5**
![Project Management](static/kanban/kanban_week_5.png)

**Week 6**
![Project Management](static/kanban/kaban_week_6.png)

**Week 7**
![Project Management](static/kanban/kanban_week_7.png)

[Go to the top](#table-of-contents)

# Wireframe
- [Balsamiq](https://balsamiq.com/) was used to create wireframes for the website. For this project, I created three different wireframes for three different devices. Balsamiq wireframe is used to create outline of the website.  

    | Page | Wireframe |
    | --- | --- |
    | Home Page | <img src="static/wireframes/home-page.png" width="600"> | 
    | Members Page |  <img src="static/wireframes/members-page.png" width="600"> | 
    | Events Page | <img src="static/wireframes/events-page.png" width="600" > | 
    | Log In Page | <img src="static/wireframes/login.png" width="600"> | 
    | Mobile |  <img src="static/wireframes/mobile-home-page.png" width="400"> | 
    | Tablet |  <img src="static/wireframes/tablet.png" width="400"> | 
 
 <hr>

### Entity Relationship Diagram

<img src="static/wireframes/Entity_Relationship_Diagram.png" width="600">

There are three main tables that are used for Events and Members entities.
Event table represents the events and Member table represents the members. There is a many to many relation between both these tables and they are linked to each other by the Event_Members table.

[Go to the top](#table-of-contents)

# Surface

 #### Color Scheme

 ![Color scheme](static/pages_screenshot/coolors.png)

 The colors used in the website are star command blue (#0077b6) for navigation bar and footer. Corn flower blue (#8ecae6) for the create new event form. Consistent white (#ffffff) background color all the pages.

 Please find the colours schemes that I used [here](https://coolors.co/0077b6-ffffff-8ecae6)

 ### Typography

 The main font used in the site is Raleway. With Sanserif as fall back font incase raleway is not imported properly. 

 The link to the font can be found [here](https://fonts.google.com/specimen/Raleway?query=raleway)

[Go to the top](#table-of-contents)

# Features

### All pages
- The navigation bar is placed at the top of all pages. The navigation bar is dynamic in that meaning depending on if the user is logged in or not the options will change.
- If the user is logged in, then the navigation bar will have all the menus:
![user_logged_in](static/pages_screenshot/navigation-1.png)
- If the user is not logged in, then the navigation bar will show only the Home, Register and Login menus:
![user_logged_in](static/pages_screenshot/navigation-2.png)

### Register Page
- A signup form which requires the member to enter username and a password. The password must be entered again for confirmation.
- Once the user has successfully signed up, they will be automatically redirected to create Member profile page.
![signup_page](static/pages_screenshot/signup-page.png)

### Login Page
- A login form that requires the user to enter their username and password that they used when signing up to the site.
- If the user enters valid username/password combination, then they will be redirected to the home page.
- If the user didn't enter valid username/password combination, then an authentication error message is shown.
![signin_page](static/pages_screenshot/signin-page.png)

### Logout Page
- When clicking Logout menu from the navigation bar, the member will be redirected to the Sign Out page.
- On further clicking the Sign Out button the user will be logged out completely and redirected to the Home page.
![signout_page](static/pages_screenshot/signout-page.png)

### Home Page
- Landing page with an image.
- An introduction about the football group in the section area.
![home_page](static/pages_screenshot/home-page.png)

### Create Profile Page
- Once the member has registered they will be redirected to the create Member profile page. 
- The page displays a form for the member to enter their first name, last name, e-mail address, telephone number and field position.
- On clicking the Create profile button the member's details are saved and redirected to the Home page.
![create_profile](static/pages_screenshot/create-profile.png)

### Create new Event Page
- Create new event Page allows members to create new event with form that consists of name, place, date and time.
![events_page](static/pages_screenshot/events-page.png)

### Event details page
- Event details page consists of Event name, Organizer, Place, Date/Time and the Members that are playing in the event.
- It also has 'Add me to this game', 'Delete me from this game' and 'Delete this game' buttons.
- 'Add me to this game' button will only be visible if the logged in user hasn't already added them to this game.
- 'Delete me from this game' button will only be visible if the logged in user has already added them to this game.
- 'Delete this game' button will only be visible if the logged in user is the user that created this event.
![event_details_page](static/pages_screenshot/event-details-page.png)

### Members page
- Members page is launched when the user clicks the Member menu.
- It lists all the Members in the group.
- Member's full name and their playing position are displayed.
![members_page](static/pages_screenshot/members-page.png)

### Edit my profile
- Edit profile page allows members to edit their profile which was created in the create profile.
- Members will be able to edit their first name, lastname and telephone number.
![edit_my_profile](static/pages_screenshot/edit-my-profile.png)

[Go to the top](#table-of-contents)

# Technologies Used

[Go to the top](#table-of-contents)

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project uses HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project uses Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project uses JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project uses Python.
-   [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    -   The project uses Bootstrap 5.
-   [PostgreSQL](https://www.postgresql.org/)
    -   The project uses PostgreSQL as a database.
-   [Gitpod](https://www.gitpod.io/)
    -   The project uses Gitpod.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project uses Chrome to debug and test the source code using HTML5.
-   [Balsamiq](https://balsamiq.com/)
    -   Balsamiq was used to create the wireframes during the design process.
-   [Google Fonts](https://fonts.google.com/)
    -   Google fonts were used to import the "Raleway" font into the style.css file which is used on all pages throughout the project.
-   [GitHub](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.

[Go to the top](#table-of-contents)

# Testing

### Navigation bar

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Home page | When clicking the home button in the navigation bar, the browser redirects me to the home page.  | PASS
Members page | When clicking the members button in the navigation bar, the browser redirects me to the members page. | PASS
Events page | When clicking the events button in the navigation bar, the browser redirects me to the events page.  | PASS
Register page | When clicking the register button in the navigation bar, the browser redirects me to the register page. The user will know they are on this page by the heading. | PASS
Login / Logout page | When clicking the login or logout button in the navigation bar, the browser redirects me to the login or logout page. The user will know they are on this page by the heading. | PASS
Text | Checked that all fonts and colours used are consistent. | PASS

### Footer
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Facebook | When clicking the Facebook icon, a new tab opens and redirects to the Facebook website. | PASS
Twitter | When clicking the Twitter icon, a new tab opens and redirects to the Twitter website. | PASS
Instagram | When clicking the Instagram icon, a new tab opens and redirects to the Instagram website. | PASS

### Home page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS

### Members page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Functionality | Check if all the registered members are listed | PASS
Functionality | Check if all the registered members full name is shown | PASS
Functionality | Check if all the registered members playing position is shown | PASS

### Events page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Functionality | Check if all the created events are listed | PASS
Functionality | Check whether Event details page is launched  when Event name hyper link is clicked| PASS
Functionality | Check whether Create Event  page is launched  when Create Event button is clicked| PASS

### Register page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Functionality | Check Username and Password fields are present | PASS
Functionality | Enter different values in the password field and check if an error message is shown | PASS
Functionality | Enter different values in the password field and check if registration succeeds | PASS
Functionality | Check if Create profile page is launched after registration succeeds | PASS
Functionality | Click Signin link and check if Login page is launched | PASS

### Event details page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Functionality | Check whether all the event details are listed corerctly | PASS
Functionality | Check whether all added members are listed correctly | PASS
Functionality | Check whether 'Add me to this game button' is visible only if the user is not already added to this event | PASS
Functionality | Check whether 'Delete me from this game' button is visible only if the user has already been added to this event | PASS
Functionality | Check whether 'Delete this game' button is visible only if the event was created by the logged in user  | PASS
Functionality | Click 'Add me to this game' button and check if the user is added to the Who's playing list | PASS
Functionality | Click 'Add me to this game' button and check if the 'Delete me from this game' is visible | PASS
Functionality | Click 'Delete me from this game' button and check if the user is removed from the Who's playing list | PASS
Functionality | Click 'Delete me from this game' button and check if the 'Add me to this game' button is visible| PASS
Functionality | Click 'Delete this game' button and check if the event is removed from the Events page | PASS


### Create event page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Functionality | Check whether error message is displayed if nothing is entered on the form and submitted | PASS
Functionality | Check whether Event is successfully created if all details are entered on the form and submitted | PASS
Functionality | Check whether Event is listed in the Events page | PASS

### Create Profile page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Functionality | Check whether Member profile form all the fields | PASS
Functionality | Check whether Member profile is saved when all the details are entered and submitted | PASS

### SignIn page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Functionality | Check Username and Password fields are present | PASS
Functionality | Enter wrong username/password combination and check if an error message is shown | PASS
Functionality | Enter correct username/password combination and check if Home page is launched | PASS

### Signout page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Functionality | Click on Logout menu and check if Logout confirmation page is launched | PASS
Functionality | Click on Logout in Logout confirmation page and check if Home page is launched | PASS

- [Validation Testing:](#validation-testing)

### Responsive Tools
[Am I Responsive](https://ui.dev/amiresponsive) was used to check if all screens are responsive to all devices.

### Html Validation:
I used [W3C Markup](https://validator.w3.org/#validate_by_input+with_options) to check for any errors within the HTML pages.
![html_validation](static/wireframes/add-html-validation.png)
Errors in the html validation could not be rectified because of the jinja template 

### CSS:
[W3C CSS Validation](https://jigsaw.w3.org/css-validator/) to check for any errors within my CSS stylesheet.

![css_validation](static/wireframes/css-validator-screenshot.png)

### Python
[PeP 8](http://pep8online.com/) to check for any errors in python code.

models.py
![pep8_validation](static/wireframes/models.py-screenshot.png)

urls.py
![pep8_validation](static/wireframes/urls.py-screenshot.png)

views.py
![pep8_validation](static/wireframes/views.py-screenshot.png)

[Go to the top](#table-of-contents)

# Bugs
- Delete this game functionality wasn't working properly.
- Edit profile page's Phone number field was having dropdown. This was fixed in the widget in forms.py
- Success page wasn't displayed for all the CRUD operations in Event and Members
- Edit profile functionality was not properly implemented
- Member's playing position was displaying None if no position entered. This was changed to 'No Position' in the template.
- Date and Time fields were not correctly captured in the Create event page. This was fixed in the template.

## Known Bugs
- Create Event page not styled properly

[Go to the top](#table-of-contents)

# Deployment

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    * In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    * In your GitPod workspace, create an env.py file in the main directory. 
    * Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    * Add the SECRET_KEY value to the Config Vars in Heroku.
    * Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    * Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    * In settings.py add the following sections:
        * Cloudinary to the INSTALLED_APPS list
        * STATICFILE_STORAGE
        * STATICFILES_DIRS
        * STATIC_ROOT
        * MEDIA_URL
        * DEFAULT_FILE_STORAGE
        * TEMPLATES_DIR
        * Update DIRS in TEMPLATES with TEMPLATES_DIR
        * Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, storage and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - Go to Deploy tab on Heroku and connect to the GitHub, then to the required recpository.
    Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.

### Forking the Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/Pavithra-Veeramani/teamer).
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

### Creating a Clone
How to run this project locally:
1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/Pavithra-Veeramani/teamer).
5. Click the green "GitPod" button in the top right corner of the repository.
This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/Pavithra-Veeramani/teamer).
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.
```
git clone https://github.com/Pavithra-Veeramani/teamer
```
8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)


<a name="end-product"></a>

[Go to the top](#table-of-contents)

# Credits

### Media

[Pexels](https://www.pexels.com/) 
- Home Page image taken by [Omar Ramadan](https://www.pexels.com/@omar-ramadan-1739260/)

### Code
[Stack Overflow](https://stackoverflow.com/) were referenced to get better ideas in order to understand and implement the code.

[Bootstrap](https://getbootstrap.com/) were referenced for the bootstrap ideas. 

[Django](https://docs.djangoproject.com/en/4.1/) was referenced for Django.

[Go to the top](#table-of-contents)

# Acknowledgements

- Thanks to my mentor Marcel Mulders for his support and feedback.

- Thanks to the tutor support in code institute for their support.

[Go to the top](#table-of-contents)


