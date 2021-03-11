# EatRank | Best guide to the best food in town

## Introduction 
EatRank is a crowd-source food review website that selects genuine customers from a community of food enthusiast to help review various restaurants in Singapore. The platform aims to moderate between the consumer’s need for credible information while balancing the anonymity of the internet which most famous reviews platform fail to moderate.

At this current stage, the idea for the platform is to have EatRank employees add partner restaurants into our platform while reviewers are verified offline via a 1-day training programme on how to utilise the platform. 

The platform aims to generate revenue from a small platform fee from restaurants and advertisements by “bumping” listings to the top of the page. 

## Demo
### You may test the current working page at: 
    https://p3-eatrank.herokuapp.com/

### No login/logout create 
This is a protocol to perform CRUD and future development will intend to allow Superuser to perform CRUD on all collections.
Each user will only be able to perform CRUD on their own listing.

## UI/UX 

### Strategy

#### __Owner Goals__
The site owner aims to use the platform to on-board partner restaurants and encourage more user sign ups. To that end, the initial phase of EatRank will allow verified users to create restaurants themselves by adding in places they have visited and wish to list on EatRank. This is to prove that the concept works and gather initial traffic to the site with an adequate number of restaurant listed.
However, this feature will be temporary and closely monitored by the Team to ensure there is no exploitation of this feature. In future, restaurants can only be added by EatRank staff.

#### __User Goals__

##### Scope 
__App features for members of the public:__
1.	A page to show all restaurants with an option to see each individual restaurant’s review. 
2.	A page to browse all reviews in the EatRank database
3.	A page to login

__App features for EatRank Community Members:__ 
1.	Log-in page 
2.	Individual review page to create/update/delete reviews made by the community member 
3.	Restaurant page to create/update/delete restaurants. 

##### User Story
For the public, they may browse (or search) for the restaurant they intend to patronise and read up on the reviews before heading down. This is done primarily on the “Restaurants” page where they may click on the review button beneath each restaurant to read the reviews.

For the public who like to read reviews casually, the “Review” page offers all the reviews, the reviewer, the rating as well as the restaurant name. This is designed for members of the public to browse and try out new places with interesting reviews. 

For community members, after logging in, they may edit their reviews by clicking on their name on the “Review” page which displays all the reviews within the EatRank database. 

Community members (upon logging in) may delete, edit or create new restaurants they visited. As mentioned in the introduction, this function is temporary.

##### Unavailable features to be implemented soon
1.  __Login/logout feature
2.	__Hashing of password.__ Currently, passwords are stored as a string in MongoDB. This feature will be done before going live. 
3.	__User/Password validation.__ Currently, there is no restrictions/limit to what a new community member can input to create an account. Technically, a new user may leave all the fields empty to sign up for EatRank. This shouldn’t be the case. For future development, validation will be included to ensure such discrepancies do not occur. 
4.	__User edit & profile picture page.__ Customisation of a user profile is a good feature to increase a community user’s ownership and commitment to the platform. Future development will include this feature where any logging in will be able to add a profile picture, a short-description and the date they joined EatRank. 
5.	__Lack of date for each review.__ This is an error discovered before submission. Date & timestamp should have been included for each review.
6.	__Bootstrap -md mosaic template error.__ One bug found during testing was the lack of responsiveness for -md for the mosaic function on the “Review” page displaying all reviews. Further investigation is warranted. Current research did not yield any results on the cause of this error.
7.	__Refined restaurant search & tag.__ One feature that was suggested but lacked the time to implement was a more refined search for restaurants. Future updates will include a “#” function for each restaurant so community users may create or follow tag trends and display those trends to the public. Restaurant may also be segmented base on their cuisine type (e.g. Japanese, Local, Fusion, Fine-Dining…) 
8.	__Footer sitemap.__ UX wise, a site map for the footer will be included in future updates. 


## Technologies used
•	HTML5

•	CSS3

•	Python 2.7.5

•	Javascript (for dependencies like Toastr & Bootstrap. No code was written in Javascript for this project)

•   Bootstrap 4.0

•   Toastr (to be implemented in future, dependecy installed)

•	Mongo Atlas 4.4

•	Cloudinary 1.22.0 

•	Flask 1.1.2

•	Flask-Login 0.5.0

•	Gunicorn 20.0.4 

•	Heroku

### Programming Methodology 
For security purposes, .env file was used together with gitignore in my working environment so that Mongo Secret and Cloudinary Secret are not pushed to GitHub.

While this project only involved myself (Daryl), I used GitHub for source control for any day-to-day commit. Commits to Heroku were done at the beginning as a test and, subsequently, nearing the deadline of the project. 

## Database Design 
Due to the simplicity of relationship between various entities, MongoDB was used for it's scalability and the infancy of this project. It is a plan, if criterions/features are confirmed and stable, for this platform to adopt SQL database which will help with enforcing relationships between data strictly as compared to MongoDB. 

Cuisine type and other search implementation are not in place due to lack of tiime.

### Database relationships

1. __Restaurants & Reviews| Many-to-many relationship__
One restaurant may contain many reviews. This is the main purpose of the application to show the reviews related to the individual restaurants. The database strategy here is to use a reference as one ID can have many reviews and inserting duplicate reviews in the review database and the restaurant will only cause the restaurant to contain a wide list of array of reviews. However, the individual restaurant is embedded into the review it is for as a reference.  

2. __Individuals & Reviews| Many-to-many relationship__
Similar to the restaurant, a reference methodology was employed so that we avoid a large array/dictionary of items/objects. 


## Testing 

### Test for CRUD 
| Step | Description            | Expected Outcomes                                                                    |
|------|------------------------|--------------------------------------------------------------------------------------|
| 1a   | View all restaurants | Click on show restaurants/ click on Restaurants to display all restaurants in database |
| 1b   | Create new restaurants | Save to database and route to display all restaurants                                |
| 1c   | Edit existing restaurant | Update, save to database and route to display all restaurants                      |
| 1d   | Remove selected restaurant | Remove from database and route to display all restaurants                        |
| 2a   | View all reviews | Display all reviews of various restaurants                               |
| 2b   | Create new review | Add new review and tag to selected restaurant                              |
| 2c   | Update existing review | Update, save to database and route to display all restaurants                             |
| 2d   | Remove selected review | Remove from database and route to display all restaurants                              |


## Deployment 
### To deploy on Heroku

1. Download or Clone the master branch from github

2. To list all the requirements in requirements.txt, run the following command in terminal:
    ```
     pip3 freeze --local > requirements.txt
    ````
3. Set Debug to False
4. Procfile need to be created to run gunicorn upon deployment

5. Git push to Heroku Master after all the documents are properly set up

6. All public keys and private keys for the following need to be added to in Heroku Config Vars settings:

    * MongoDB URI
    * MongoDB Secret Key
    * Dabatase Name : EatRank
    * Cloudinary Upload Preset
    * Cloudinary Cloud Name

## Credits 
1. __Freepik Premium Content Provider:__ Much of this project relied on Freepik image provider for the hi-res images on the beginning of the page. As the account used is premium, no attribution was required and it is free to use.
2. __GetBootstrap.com:__ Bootstrap 4.0 was used for much of the layout for the flexbox & styling of individual reviews/restaurants,login pages and icons (did not rely on fontAwesome for this project).
3. __Paul Chor:__ Provided the boiler plate template for Flask and mentorship for the whole of the project's life-cycle.
4.  Google for some famous restaurants and use their picture for project purpose
5.   www.unsplash.com - free images
6.   w3school - references
7.   stackoverflow - references
8.   FontAwesome - free fonts & logos





