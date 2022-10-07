# Proposal

## Name
smite.gg

## Project Overview
### Major features
#### mvp
-retrieve current data from smite api
-display data in an organized way (gods, items, player stats)

#### next
-use god stats to show base stats 


### attempt to solve
-replace slower website similar that experiences a lot of down time

### libs/frameworks
-django
-vue
-bootstrap
**axios**/**request **/

## Features
-as a user I want to see gods and items
-as a user I want to be able to search for a player
-as a user I want to see a players over stats, rank stats
-as a user I want to see a players match history

## Data Model
-django.user
-godSkins
    -godIcon_URL
    -godSkin_URL
    -god_name
    -god_id


## Schedule
### week 1
-setup navigation to all pages needed blank with just name
-auth, models
-api functioning in a non expensive way

### week 2
-displaying all data correctly on templates with vue
-god page
-item page
-player search results page
-player page

### week 3
-refine/refactor
-styling