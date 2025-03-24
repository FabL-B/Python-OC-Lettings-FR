Views, URLs and Templates  
=========================

This section describes the main routes of the application, the associated Django views, and the HTML templates used.

Main Pages  
----------

- **Home**

  - **URL**: `/`
  - **View**: `oc_lettings_site.views.index`
  - **Template**: `index.html`

- **404 Error Page**

  - **View**: `oc_lettings_site.views.custom_404`
  - **Template**: `404.html`

- **500 Error Page**

  - **View**: `oc_lettings_site.views.custom_500`
  - **Template**: `500.html`

Lettings  
--------

- **Lettings List**

  - **URL**: `/lettings/`
  - **View**: `lettings.views.index`
  - **Template**: `lettings/index.html`

- **Letting Detail**

  - **URL**: `/lettings/<int:letting_id>/`
  - **View**: `lettings.views.letting`
  - **Template**: `lettings/letting.html`

Profiles  
--------

- **Profiles List**

  - **URL**: `/profiles/`
  - **View**: `profiles.views.index`
  - **Template**: `profiles/index.html`

- **Profile Detail**

  - **URL**: `/profiles/<str:username>/`
  - **View**: `profiles.views.profile`
  - **Template**: `profiles/profile.html`
