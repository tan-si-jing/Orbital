# Orbital
Proposed Level of Achievement: Project Apollo

# Motivation

When you’re preparing an upcoming trip, much time is inevitably spent on planning. It is a chore to many, and often results in toggling between many tabs and different applications, as well as difficulty organising all the research and putting together a neat, customised itinerary. The sheer amount of effort required in planning a trip makes it seem like an insurmountable task and takes out the fun of the adventure itself. This could be especially overwhelming for inexperienced travellers who do not know where to start.

Aside from researching and deciding on places to go, it is also time-consuming for travellers to attempt optimising the travelling route for the trip. On the other hand, without the optimisation of routes, precious time would be wasted on detours when travelling to locations in the wrong order. More often than not travellers are required to switch between many applications, such as online maps for directions, websites for suggestions of nearby places to visit, or a document containing the itinerary. 

We aim to streamline the process by merging all the functionalities into one website, thereby making the planning of trips more efficient and less tedious.

User Stories:
- As an inexperienced traveller who wants to plan for my next trip, I want to be able to spend less time planning and reduce the amount of research required while creating an optimal and organised itinerary that suits my needs.
- As a tourist who is not familiar with the country I am travelling to, I want to be able to optimise the routes so as to maximise my time, as well as receive suggestions of nearby places to go, tailored according to the purpose of my trip.
- As an experienced traveller, I want to have the flexibility to plan my own travels, with the convenience of having both suggestions for nearby places and directions all in one place which I can access on-the-go.
- As a user who is travelling and planning with others, I want to be able to share my itinerary with other users.



# Project Scope

The website allows users to create and share itineraries, including features such as route optimisation, directions and suggestions of locations to organise and optimise the itinerary.

Globetrotter is a fuss-free itinerary planner that does the dirty work of planning for users and is suitable for those inexperienced with planning trips or users who simply do not want to spend so much time planning. Globetrotter allows you the flexibility to be as hands-on as you wish and suggestions are personalised according to users’ activities preferences. Not only does it allow users to organise their itinerary, it also provides a route optimisation tool and directions to reduce the time unnecessarily wasted on travelling. All the features packed into one website reduces the need to access many different applications at the same time, streamlining the process to allow users to spend less time planning and more time enjoying themselves.

What sets us apart? 
- Spreadsheets (Excel or Google Sheets)
While it allows proper organisation of the itinerary, it is less readable when storing more information in each cell. While using a word document could be an alternative, it is linear and less organised. In addition, all these methods do not provide additional features to improve the travel experience such as route optimisation.

- Existing itinerary-building websites
While it is more suitable for creating and organising itineraries as it is more readable, it is similar to using spreadsheets in that they do not have the additional features mentioned above. Also, they do not cater to travellers of different requirements, where some are too rigid and others too unguided.

- Existing route-optimisation websites
It does not provide suggestions of nearby locations that are tailored to users’ activities preferences. It is also unable to store the itinerary to be edited at a different time, changes are lost when the user closes or refreshes the page.



Enter the country, city and date of travel to begin, and organise your trip and slot activities neatly into each column. A handy button in the sidebar will suggest to you nearby attractions, sightseeing, entertainment and shopping facilities. You can edit and add things to do to your trip, and we will suggest the most efficient route to take for travelling around in each specific day to all your selected locations.


# Core features

Features completed for Milestone 2:
  - Login/Registration of users
  - Display page for created itineraries (message is displayed instead if user has yet to create any itinerary)
  - Basic template for creation of itineraries
  - Creating and organising locations/activities in the itinerary
  - Sharing itinerary with other users

Features completed for Milestone 3:
  - Display of all itineraries created and all itineraries that are shared with the user
  - When an itinerary is created by the user, or an itinerary is shared with the user, it will appear as an interactable animated icon on the user’s dashboard page. When clicked upon, it redirects the user to the respective itinerary
  - Permission sharing itinerary with other users through email address
  - When a permission sharing request is granted, an email will be sent to the email address and the itinerary can be edited by the user 
  - A separate column on the itinerary editing page
  - Users can drop and drop their activity boxes into the sort column
  

# System testing

Login/Registration of users
- Prevents invalid input such as invalid name and email format or empty fields
- Each email is only allowed to be associated with one account
- System will flash relevant error messages and disallow the completion of the registration process
- Passwords are encrypted in database to ensure security
- Certain webpages (such as itinerary dashboard) are only accessible to users who are logged in. Manually keying in the website link to these pages will redirect them to the login page with a prompt to login

Creation of itineraries:
- Prevents invalid input such as empty fields in the creation of itineraries and the items inside itineraries 
- Itineraries will only be viewable to the users whose emails have been shared by the original creator of the itinerary
- Editing of itineraries
- Prevents unauthorised users from deleting, editing, or rearranging the components inside itineraries
- Edit will not be saved if there is an invalid input (such as an empty field in a column) in the contents of the itinerary
- Refreshing the page will retain positions of all items
- Permissions can be granted for other users to view and edit the itinerary

# Tech Stack
- HTML/CSS/Javascript
- jQuery and AJAX
- Flask
- MySQL

# Project Video
https://vimeo.com/442115748
