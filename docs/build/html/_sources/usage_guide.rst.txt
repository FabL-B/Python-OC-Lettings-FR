Usage Guide  
====================

This section presents some typical use cases of the application.

Accessing the Home Page  
---------------------------

- Open your browser and go to: http://127.0.0.1:8000/  
- This page contains links to the “Lettings” and “Profiles” sections.

Viewing the Lettings List  
-------------------------------

- Click on the “Lettings” link from the home page.  
- The URL becomes: http://127.0.0.1:8000/lettings/  
- The user sees a list of available lettings.  
- Clicking on a letting redirects to its detail page.

Viewing a Letting  
---------------------

- Example URL: http://127.0.0.1:8000/lettings/1/  
- This page displays:  
  - The letting title  
  - The full address  
- This view corresponds to `lettings.views.letting`

Viewing the Profiles List  
-----------------------------

- Click on the “Profiles” link from the home page.  
- The URL becomes: http://127.0.0.1:8000/profiles/  
- The user sees a list of user profiles.  
- Clicking on a profile redirects to its detail page.

Viewing a Profile  
---------------------

- Example URL: http://127.0.0.1:8000/profiles/JohnDoe/  
- This page displays:  
  - The username  
  - The favorite city of the user  
- This view corresponds to `profiles.views.profile`
