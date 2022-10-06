# FitYou

FitYou is a fitness app made with features to **FitYou** to help you achieve your fitness goals! With features ranging from personalized calendars, recipes, and workout splits! Using Api's the app will give the user recommendations for meals and workouts, and then allow these meals and workouts to be added to the calendar for easy tracking!


# Features

**Calendar**
- The ability to plan out days, weeks, or even a months worth of splits
- Customized notes attached to each calendar day to help you plan out splits and reminders!
- Allows users to revisit previous splits by the weeks, idea is to give the user the chance to customize splits.

**Workouts**
- Inside of the workout feature users can search muscle groups by keyword, and is given a list of popular/common exercises used to target that muscle group
- This workouts can now be added to the calendar 

## Additional Features  
**Intensity**
- I would like to add a feature that allows the user to choose the level of intensity per workout, using stored data from similar workouts and then multiplying the weight from previous workout by set percentage. 
- The reps will be set in a 6/8/12 split

**Quotes/Reminders** 
- Beginning and the end of each workout, a simple stretch reminder (y/n), with a random motivational quote  

**Goals**
- A page to help keep track of weight goals you've set and/or surpassed 

**Favorites**
- When an exercise is fav'd it will be auto added to workouts in that muscle group or by split ('Chest", "Back")

**Recipes**
- A separate page dedicated to the nutrition part of a healthy lifestyle!
- Search recipes by keyword ingredients
- This recipes can now be added to the calendar

## Models

- userModel
	>- (sign in, sign up, auth)
- workoutModel
	>- (weightUsed, exerciseUsed, repsUsed.)
- userWorkout
	>- (fav, date stored here, notes, addToCalendar)

# Schedule


- **Week 1**
	>- Create the search ModelForm to get exercises from the api
	>- create the models and attributes 
	>- display the calendar with content 

- **Week 2**
	>- adding workoutModel and userWorkout attributes to calendar
	>- create the intensity logic in the workoutModel

- **Week 3**
	>- Add a logo if possible
	>- add photos to the different features 
	>- debug
	>- deploy?
	


	

