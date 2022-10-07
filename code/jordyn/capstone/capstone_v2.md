### Slothypoo Art Gallery

My web application is meant to fulfill the need for my sister to present her artwork online. All artists need somewhere to advertise themselves, and I want to fulfill that need for her! The application will not feature a lot for a general user to see, with only a couple pages that show off artwork and commission info. The Admin page will be private and the focal point of this project. It will feature the ability to add new drawings and give them attributes for smarter display throughout the rest of the application.

The art gallery will use Django, Python Pillow, Javascript, and Vue. There is a possibility of the use of bootstrap as well, namely the Card bootstrap. Python Pillow is an image manipulation library that will be used to automatically generate smaller versions of the original upload to be used instead when the full sized image is not needed. Examples: Commission Page which has small previews for each type of artwork, or the Gallery before the image is made larger on click


## Data Model

This project will need a way to save an image and give it other details attributed to it alone. The details I have planned are:
- Image name (And subnames from Python Pillow)
- Date Submitted
- Defining Tags (The type of artwork being represented)
- NSFW Tag (Some things are better for at home)

The Image name will either be a name chosen by the user or an automatic name that utilizes a number generated for it, preferably the first option

Date Submitted will represent the moment that the image was uploaded, this will be useful for ensuring that the Gallery can list off artwork by order of submission

Defining Tags would be used to further sort the artwork for browsing users. Examples of this could be Line Art (Artwork without color and shading) or Full Color (Artwork with all the bells and whistles). This will allow users to find artwork relevent to the style they are considering for commission work.

## Schedule

Due to the nature of this application, creating the MVP will be somewhat of a long term goal. The two minimal working parts needed would be the Admin Page and the Gallery Page. With that in mind I will be following this schedule order and proposed timeline:
- Week 1:
    - Admin Page (7+ days)
        - Upload implementation
        - SQLdatabase setup
        - Submission Edits Menu
- Week 2:
    - Gallery Page (3-5 days)
        - Display Artwork
        - Sorting Menu
        - MVP Milestone
    - Contact Info Page (Main Page) (1 day)
        - Displays multiple ways to contact artist or view social media
- Week 3:
    - Commission Page (1 day)
        - Displays basic info on commission options
    - TOS Page (1 day)
        - What the artist will draw and what they allow the commissioners to do with finished products
    - Finalize CSS and Javascript 

## Additional Features

Should time allow, a modified To-do List is another feature I would like to add. This list would show basic information for the Artist and the User about current and future Commissions being handled.

The Users would see:
- Commissioner Handle
- Artwork Type
- Start Date
- End Date

The Artist would see:
- Commissioner Handle
- Artwork Type
- Start Date
- End Date
- Payment 1
- Payment 2

Seperate Payment info is because payments are done half and half. Half upfront, half on completion

This could prove to be a large project on its own, so I will be leaving this to the very end if I find myself with additional time and a product I am happy with.