# Dine Diary

## Project Overview
  There are so many options for eating out at restaurants, whether they’re fine dining or fast food. Restaurants you have already been to can be hard to keep track of given that you visit them over longer periods of time, so having a way to organize the information would be helpful. 
  
  Our application allows users to input their restaurant visits, including the dishes they ordered, so they can refer back to the application when recommending or revisiting a spot. It includes user information like name, email, a unique user id, etc. The restaurant information that is tracked includes the cuisine, overall rating, the general price range, etc. The users also have the ability to input the name of the dish they got, thoughts on presentation, and a review of the dish as well as the menu. For user using this application to achieve fitness/health goals there is also an option to input nutritional information. 
  
  Aside from being able to keep track of restaurants visited in an organized and efficient manner, this application also allows users to share their experience with fellow peers through a social-media style UI. Users have the option to post pictures, leave comments and reactions, and make foodie-friends on the app! 
  
  This app has potential to revolutionize the way that people keep track of their favorite spots and the specific dishes they enjoyed at those spots. We expect a wide variety of users to be able to use the app regardless of age, dietary preferences, and other factors. 

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 




