# Vélo City E-Commerce Website

## Introduction

![Image of Device responsiveness](media/images/readme/amiresponsive2.png)

Vélo City is an e-commerce cycling website where users can purchase bikes and cycling kit. 

There are two types of users, for which the test account details are as follows:
* Admins:
Username: superuser
Password: password4963!

* Shoppers/regular users:
Username: rosuper
Password: password4963!

Visit the live site here: https://velo-city-rc.herokuapp.com/

## Table of Contents

- [Vélo City E-Commerce Website](#v-lo-city-e-commerce-website)
  * [Introduction](#introduction)
- [User Experience (UX)](#user-experience--ux-)
  * [Strategy](#strategy)
    + [Business Model](#business-model)
    + [Marketing](#marketing)
    + [Search Engine Optimisation](#search-engine-optimisation)
    + [Project Goals](#project-goals)
    + [Site Owner's Goals](#site-owner-s-goals)
    + [Site User's Goals](#site-user-s-goals)
    + [Target Audience](#target-audience)
  * [Structure](#structure)
    + [Website Pages](#website-pages)
    + [Database](#database)
  * [Scope](#scope)
  * [Skeleton](#skeleton)
    + [Wireframes](#wireframes)
    + [Surface](#surface)
    + [Colour Scheme](#colour-scheme)
    + [Typography](#typography)
    + [Imagery](#imagery)
- [Features](#features)
  * [Existing Features](#existing-features)
  * [Features to implement in future](#features-to-implement-in-future)
- [Technologies Used](#technologies-used)
  * [Languages:](#languages-)
  * [Frameworks, libraries and programs used:](#frameworks--libraries-and-programs-used-)
- [Deployment](#deployment)
  * [Amazon Web Services](#amazon-web-services)
  * [Local Deployment](#local-deployment)
  * [Heroku and Postgres](#heroku-and-postgres)
- [Testing](#testing)
  * [Testing User Stories](#testing-user-stories)
    + [General User Stories](#general-user-stories)
    + [Feature User Story Testing](#feature-user-story-testing)
  * [Validator Testing](#validator-testing)
  * [PEP8](#pep8)
  * [JSHint](#jshint)
  * [Lighthouse Testing](#lighthouse-testing)
  * [Further Testing](#further-testing)
  * [Bugs](#bugs)
- [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Images](#images)
- [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# User Experience (UX)

## Strategy

### Business Model

The business model behind Vélo City is B2C or Business to Customer. The online store sells products from various cycling brands rather than their own branded products.

In terms of the flow of the business model, Vélo City buys all products from their affiliated brands and manufacturers, and these products are then sold via the Vélo City website to the customer.

The flow of the B2C model can be illustrated as follows:

![B2C Chart](media/images/readme/b2c-flowchart.png)

Typical required features of the B2C model include:
 * A strong advertising stratgey to attract customers.
 * High investment in terms of hardware/software.
 * An excellent standard of customer service.

### Marketing

Vélo City has a Facebook Business page which can be viewed [here](https://www.facebook.com/V%C3%A9lo-City-105357878885354"). This can also be accessed from the footer of the website.

The Facebook page is set up with the intention of posting regularly to gain engagement from followers, from silly relatable day-to-day posts, to announcing new stock, offers and deals.

The website footer also contains a Mailchimp marketing comms subscription sign up form. When users sign up to the Mailchimp form, their details feed through the company's Audience Dashboard on Mailchimp account. These customers can now be included in Vélo City marketing campaigns. 

As these marketing strategies involve the collection of user data, to ensure that Vélo City adheres to GDPR standards, there is a Vélo City Privacy Policy which can be found on the footer of the website.

### Search Engine Optimisation

This project includes a Sitemap.xml and Robots.txt file to ensure that Google can crawl only the relevant and unique pages of the Vélo City website.

I have also researched the top search terms for bike store products, for which I used Google search and Wordtracker.com, in addition to reviewing other cycling e-commerce sites, such as ThinkBike.ie.

Wordtracker results example:
![Wordtracker results example](media/images/readme/wordtracker-example.png)

The following site description, keywords and key phrases were included in the project meta tags:

![SEO description and keywords](media/images/readme/seo-keywords.png)

Where possible, images were also re-named to be SEO-optimized, e.g. updated from names with no meaning attached to terms which would help the SEO rating of a cycling e-commerce site.

### Project Goals

* To create an e-commerce cycling website which sells bikes and cycling kit. The site also features a cycling blog and events page which aims to attract cyclists to the site, and keep potential shoppers interested so that they might spend more time on the site.

### Site Owner's Goals

* To allow users to purchase products on the site.
* To add, edit and update products on the site. 
* To add, edit and update blog posts which are published for site users.
* To add, edit and update event posts which are published for site users.
* To allow users to book a bike service via the site. 

### Site User's Goals

* To purchase bikes and cycling kit.
* To view the site blog posts for cycling tips.
* To get information about upcoming Irish cycling events via site event posts. 
* To book bike services.
* To login or logout of the site.
* To easily recover my password if I forget it
* To register as a user of the website and receive a confirmation email when doing so.
* To have a personalised profile which contains my order history, delivery and payment information.
* To sort the list of available products by category, price and rating.
* To complete a purchase of products in a shopping cart.
* To search for a product by category, name or description and view the search results.
* To view a list of products on the website.
* To view a product detail page for each product (image, price, description, category, rating and size).

### Target Audience

* Anyone who is interested in purchasing a bike or cycling kit, especially cycling enthusiasts who are likely to enjoy the cycling content, return to the site and develop brand loyalty.

## Structure

### Website Pages

The website contains the following pages: 

 * Home page

 * About page

 * Products page

 * Product detail page

 * Blog list and blog detail pages

 * Events page

 * Log in/out and register pages

 * Product Management Pages (Add, Edit and Delete)

 * Blog Managements Pages (Add, Edit and Delete)

 * Events Management Pages (Add, Edit and Delete)

 * My profile page

 * My Cart page

 * Checkout page

 * Checkout success page

For consistency of user experience, the site logo, navigation links and footer remain consitent throughout the site.

### Database

* The website uses HTML, Javascript and CSS used with the Bootstrap framework for the frontend.
* The backend was created using Python, built within the Django framework and uses the Postgres database for the deployed Heroku version.
* A SQLLite database was used for local development.

**Physical database model** 

![Database](media/images/readme/pp5-database.png)

* Post model

  * The Post model contians information about blog posts posted to the website. 
  * It contains author as a foreign-key for the users table.
  * The model contains the following fields: title, slug, author, updated_on, content, created_on, status, image_url, and image.

* Event model 

  * The Event model contains information about event listings posted to the website.
  * The model contains the following fields: title, event_category, event_date, updated_on, content, created_on, status, image_url and image.
  * The model contains multiple category types which can be chosen from a drop down menu when a post is being created.

* Booking Model
  
  * The Booking model contains information about bike service bookings made by site users.
  * The model contains the following fields: first_name, last_name, email_address, phone_number, date, and service_type. 
  * Service type field contains several choices which appear within a dropdown menu on the front-end of the site. They are: Bike fit, Repair and Full service.

* User Model

  * The User model contains information about the user. It is part of the Django allauth library.
  * The model contains the following fields: username, password, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, date_joined.

* UserProfile Model

  * The UserProfile Model contains information about the user's profile. It has a one to one relationship with the user.
  * The model contains the following fields: user, default_phone_number, default_street_address1, default_street_address2, default_town_or_city, default_county, default_postcode, default_country.

* Product Model

 * The Product model contains information about all products on the site.
 * The model contains the the following fields: category, sku, name, description, has_sizes, price, rating, image_url and image.
 
* Category Model 

  * The Category model contains a product's category.
  * The model contains the following fields: name and friendly_name.

* Order Model 

  * The Order model contains information about a customer's order.
  * The model contains the following fields: order_number, user_profile, full_name, email, phone_number, country, postcode, town_or_city, street_Address1, street_Address2, county, date, delivery_cost, order_total, grand_total, original_cart and stripe_pid.

* OrderLineItem Model  

  * The OrderLineItem model contains information about an entry in an order, for orders made on the website.
  * The model contains Order and Product as foreign-keys.
  * The model contains the following fields: order, product, product_size, quantity and lineitem_total.

## Scope

* First Time Visitor Goals

  * As a First Time Visitor, I want to easily understand the purpose of the site.
  * As a First Time Visitor, I want to easily navigate throughout the site to find content.
  * As a First Time Visitor, I want to easily find information about the company.
 
* Returning Visitor Goals

  * As a Returning Visitor, I want to easily access and navigate to the different product links, my profile and the blog, event and booking pages.
  * As a Returning Visitor, I want to easily access the company's social media links so that I can follow them and keep up to date with news and offers.
  
* Frequent User Goals

  * As a Frequent User, I want to be able to access the site from any device including mobile, even if I am on the go.

* Site Owner Goals

  * As a site owner, I want to create an a stylish and visually appealing website which elicits a positive emotional response in users.

  * As a site owner, I want to create easy to use website where products and their categories can be easily found and purchased.

  * As a site owner, I want to convey an impression of expertise on the sport of cycling and cycling products so that I can gain customer's trust and loyalty.

  * As a site owner, I want to have a good marketing strategy, including easily found social media links and a marketing email subscription option.


More specific user stories are discussed in the context of website features in the Features section below.

Note: Throughout the project, this [Kanban board](https://github.com/rocrill/velo_city/projects/1) was used to organise and track the progress of the user story development as part of the Agile development approach. However the final more detailed user stories are documented fully within this Readme. For reference, the applicable Kanban user stories have been linked to their corresponding README user stories below.

## Skeleton

### Wireframes

Wireframe mock-ups were made using Balsamiq to help plan and visualise the site design. They were created for 2 main screen sizes: desktop and mobile.

Desktop:

- [Desktop wireframes](docs/vc-wireframes-desktop.pdf): Desktop wireframes

- [Mobile wireframes](docs/vc-wireframes-mobile.pdf): Mobile wireframes


### Surface

### Colour Scheme

The colour palette chosen for the website is intended to be subtle and sophisticated. The palette was chosen using the Coolors colour generator website.

![Image of Colour Palette](media/images/readme/palette.png)

The colours mainly used were:

#283D3B - Outer Space Crayola

#197278 - Skobeloff

#EDDDD4 - Champagne Pink

#C44536 - International Orange Golden Gate Bridge

Black and White were also used in different parts of the site to achieve the best possible contrast for user experience.

### Typography

'Bodoni Moda', taken from Google Fonts, is the main font used throughout the website with 'Sans Serif' as the fallback font. 

### Imagery

All images were sourced from [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/). It is a clean and elegant font which works well across the site on all screen sizes.

# Features

## Existing Features

**Feature 1. Navigation bar**

  * The navigation bar is at the top and centre of all pages of the website for consistent user experience and so they can navigate easily.

  * A pointing hand icon appears over the menu links when they are hovered over for responsiveness.

  * On the drop-down menu for each main navigation link, each drop-down option is highlighted in grey when hovered over for responsiveness.

  * On mobile, the navigation menu links are within a collapsed drop down menu instead of in-line.


  Desktop:

  ![Image of desktop nav menu](media/images/readme/navigation-desktop.png)

  Tablet:

  ![Image of tablet nav menu](media/images/readme/navigation-tablet.png)

  Mobile:

  ![Image of mobile nav menu](media/images/readme/navigation-mobile.png)

 

User stories relating to Navigation bar and home page:

  * 1.1 As a user, I see the navigation bar with a logo on all pages and with a search box on a desktop, tablet and mobile.
  * 1.2 As a user not logged in, I see a Register/Login link in the nav bar. Clicking this leads me to the registration or sign in pages and enables me to register or sign in (#6 and #7).
  * 1.3 As a logged in user, I am notified when I am logged in and I see a logout link in the nav which enables me to click sign out which logs me out.
  * 1.4 As a user, I can easily receive email confirmation after registering so that I can verify that my account registration was successful (#9.
  * 1.5 As a user I can view the website logo in the header at all times, and clicking this will bring me to the homepage.
  * 1.6 As a user I can click the all product, service, blog and event nav links which bring me to the relevant pages.
  * 1.7 As a user if I encounter an error on the site, an applicable error message will be shown.
  * 1.8 As a user, I can easily recover my password if I forget it so that I can easily get into the site if I forget my password without re-registering (#8).
  * 1.9 As a user, I can have a personalised user profile so that I can view my order history, order confirmations, saved favourite products and save my payment information(#10).
  * 1.10 As a user, I can search for a product by name or description so that I can easily find specific products that I want to purchase (#14).
  * 1.11 As a shopper, I can easily see what I've searched for and the number of results so that I can quickly decide if the product I want is available (#15).
  * 1.12 As a user, I cannot access areas of the site that are restricted to admin users, and I receive an appropriate error message when I try to do so.


**Feature 2. Home page**

  * The home page features a bike 'hero' image and a centrally placed call to action 'shop now' button which takes the user to the all products page.

  Desktop:

  ![Image of desktop home page](media/images/readme/homepage-desktop.png)

  Mobile:

  ![Image of mobile home page](media/images/readme/homepage-mobile.png)

User stories relating to the Home page:

  * 2.1 As a user, I want to see a homepage to contain a navigation bar and footer which clearly direct me to all available site pages.
  * 2.2 As a user, I want to see call to action button which directs me to the primary purpose of the site - to shop.
  
**Feature 3. All products page**

  * The all products page is neat and well-proportioned with 4 product cards spanning the width of the page. Each product card contains the product name, rating, price and category label. 
  * The all products page is paginated so that when more than 8 products are added to the site, the button appears directing the user to a second page of additional products, and so on.
  * The mobile all products page is adjusted to feature one column of prodct cards across, and eight cards appear before thr pagination button is displayed. 
  * There is a sorting drop-down menu on the top of the page which allows the user to sort products by price (low to high), price (high to low, name (A-Z), name (Z-A), rating (high to low), rating (low to high), category (A-Z) and category (Z-A).

  Desktop:

  ![Image of desktop all products page](media/images/readme/all-products-desktop.png)
  ![Image of desktop all products page](media/images/readme/all-products-desktop-2.png)

  Mobile:

  ![Image of mobile all products page](media/images/readme/all-products-mobile.png)
  ![Image of mobile all products page](media/images/readme/all-products-mobile-2.png)

User stories relating to the All Products page:

  * 3.1 As a user, I want to see a neatly displayed list of products with visually appealing images, clearly listing the name, price, category and rating of each product so I can decide on which products to view more detail on based on whether they are popular, relevant and within my price range (#1, #2, and #3).
  * 3.2 As a user if there are more than 8 products on the page, the page is paginated in order to maintain the neat look of the site and to avoid endless scrolling for the user.
  * 3.3 As a user, I want to quickly identify offers and deals so that I can get the best value (#4).
  * 3.4 As an admin, I want to be able to edit or delete products from the all products page.
  * 3.5 As a user, I can sort the list of available products so that I can easily identify the best value, best rated and categorically sorted products (#11).
  * 3.6 As a user, I can sort a specific category of product so that I can find the best-priced or best-rated product in a specific category, or sort by name in that category (#12).
  * 3.7 As a user, I can sort multiple categories of products simultaneously so that I can find the best-priced or best-rated products across broad categories, such as "clothing" and "accessories" (#13).


**Feature 4. Category-specific product page**

  * The navigation menu contains drop-down options to all product categories for bikes and clothing which directs the user to a category specific product page, e.g. Vintage Bikes. The page layout for each category is the same as the all products page on desktop and mobile. The product cards contain the same information, and users can sort by the same options.
  * When on a category-specific product page, the category is displayed in a box at the top of the page so that the user is aware which specific product page they are on.

  Desktop:

  ![Image of desktop category specific products page](media/images/readme/category-specific-product-page-desktop.png)

  Mobile:

  ![Image of mobile category specific products page](media/images/readme/category-specific-product-page-mobile.png)

  User stories relating to the category-specific products page:

  * 4.1 As a user, I want to be able to easily access a catergory-specific product page so that I can access the content that I am interested in quickly and easily.

**Feature 5. Product Detail page**

  * This contains a product image, description, price, category label, and rating.
  * Beneath the description there is a dropdown menu to select the size of the item. Underneath this there is a link to a size guide pdf for bikes and clothing. 
  * Beneath the size selection there is a button to select the quantity of the item you would like, and a button to add this to your shopping cart.
  * Links to edit and delete the post will also appear here if an admin user is logged in.
  * At the bottom of the page is a 'You May Also Like' recommended products feature. This displays other products within the same category that the user may be interested in.

 Desktop:

  ![Image of desktop product detail page](media/images/readme/product-detail-desktop-1.png)
  ![Image of desktop product detail page](media/images/readme/product-detail-desktop-2.png)

  Mobile:

  ![Image of mobile product detail page](media/images/readme/product-detail-mobile-1.png)
  ![Image of mobile product detail page](media/images/readme/product-detail-mobile-2.png)

  Size Chart:
 ![Image of size chart](media/images/readme/size-chart.png)

  User stories relating to the product detail page:
  
  * 5.1 As an admin user, I want to be able to edit or delete a product from the detail page so that I can easily edit products as an admin.
  * 5.2 As a user, I want to be able to view all product information on the product detail page including an image, price, rating, category, description and size.
  * 5.3 As a user, I want to be able to view a size chart for the product I am interested in so that I can be sure I am selecting the correct size for myself (#40).
  * 5.4 As a user, I want to be able to select the quantity of items I want and put a product in my shopping cart directly from the product detail page so that I can shop efficiently (#16).
  * 5.5 As a user, I can see similar/recommended items so that I can enjoy a personalised shopping experience and be aware of the products I am most likely to like and purchase (#28).


**Feature 6. Service Booking page**

* This page contains a description of Vélo City's service offering and a form for the user to request their desired service.
* The service booking form contains a dropdown of available service types and a calendar widget to select the desired service date.
* Once a user submits the form requesting the service, they receive a notification that the form is submitted, and that a member of the Vélo City team will be in touch to confirm their appointment.

  Desktop:

  ![Image of desktop service booking page](media/images/readme/book-service-desktop.png)

  Mobile:

  ![Image of mobile service booking page](media/images/readme/book-service-mobile.png)

  User stories relating to the Service Booking page:
  
  * 6.1 As an user, I want to be able to book a bike service easily and efficiently, so that I can arrange to resolve an issue with my bike quickly and easily (#26).
  * 6.2 As a user, I want to receive a confirmation message so I know that I have successfully submitted my booking form.
  * 6.3 As a user, I want to receive a notification if I have accidentally selected a booking date in the past so I know that I need to fill out the form again.

**Feature 7. Blog**

* Vélo City contains a blog which offers cycling tips and guides. The aim of the blog is to position Vélo City as an expert in the world of cycling and to attract cyclists to the site for blog posts, who will then be introduced to the business and its product offering.
* The blog post list is paginated so when more than three posts are published a button appears to continue to the next page of posts.

  Desktop blog post list page:

  ![Image of desktop post list page](media/images/readme/blog-postlist-desktop-1.png)
  ![Image of desktop post list page](media/images/readme/blog-postlist-desktop-2.png)

  Desktop blog post detail page:

  ![Image of desktop post detail page](media/images/readme/blog-postdetail-desktop-1.png)
  ![Image of desktop post detail page](media/images/readme/blog-postdetail-desktop-2.png)
  ![Image of desktop post detail page](media/images/readme/blog-postdetail-desktop-3.png)

  Mobile blog post list page:

  ![Image of mobile post list page](media/images/readme/blog-postlist-mobile.png)

  Mobile blog post detail page:

  ![Image of mobile post detail page](media/images/readme/blog-postdetail-mobile-1.png)
  ![Image of mobile post detail page](media/images/readme/blog-postdetail-mobile-2.png)


  User stories relating to the Blog:
  
  * 7.1 As an user, I want to be able to access blog content with cycling tips and guides so that I can improve my knowledge of cycling and become a better cyclist (#31).

**Feature 8. Events Page**

  * Vélo City contains an events page which lists upcoming cycling events which may be of interests to our site users. These incude events that Vélo City is a part of, as well as cycling events around Ireland. 
  * There are four categories of events: Mens cycling, Ladies cycling, Racing and Social events. Users can filter the events by category.
  * The Events list is displayed in order of the nearest event date first so that users can see what event is the soonest straight away.

  Desktop event list page:

  ![Image of desktop event list page](media/images/readme/event-list-desktop.png)

  Mobile event list page:

  ![Image of mobile event list page](media/images/readme/event-list-mobile.png)
  
  User stories relating Events list:

    * 8.1 As a user, I want to see a list of upcoming Irish cycling events so that I can engage with the cycling community and potentially take part in competitive events (#33).
    * 8.2 As a user, I want to be able to filter the cycling events for categories that are relevant to me.

**Feature 9. Shopping Cart and Checkout**

  * If the user has not added an item to the cart and they navigate to the cart page, they see a message that the cart is empty.
  * The user can add items to their shopping cart as they are shopping. They receive notifications when they have done so. 
  * The shopping cart shows an image of each item added, along with its quantity and price. The subtotal of all items is also calculated.
  * On the shopping cart page the user can reduce or the increase quantity of each item, or remove the item completely. 
  * An order over €50 entitles the shopper to free delivery, the delivery charge is automatically calculated at the checkout page.
  * Once an order is made, the user receives a confirmation email.
  * The fields on the checkout page are: Full Name, email address, phone number, and address and Country fields. This information is populated from 'my profile' if filled in.
  * Even if a user is not logged in, they can add products to their bag and proceed to checkout.

Desktop checkout page:

![Image of desktop checkout page](media/images/readme/desktop-checkout-page.png)

Mobile checkout page:

![Image of mobile checkout page](media/images/readme/mobile-checkout-page.png)

Desktop shopping cart:

![Image of desktop shopping cart](media/images/readme/desktop-cart.png)

Mobile shopping cart:

![Image of mobile shopping cart](media/images/readme/mobile-cart-1.png)
![Image of mobile shopping cart](media/images/readme/mobile-cart-2.png)

User stories relating to the shopping cart and checkout:

  * 9.1 As a user, I can click on a product, select a size and quantity and add it to my bag (receiving a notification when I've done so) in order to purchase it. 
  * 9.2 As a user, I can click on the cart icon and be brought to my bag to see the contents in order to know what I have selected so far and the subtotal. If no contents are there, I will see a message that the cart is empty (#17).
  * 9.3 As a user, I can update the quantity or remove an item from my shopping bag (#18).
  * 9.4 As a user, I can click on the Secure Checkout button on the cart page or toast message, and will be directed to the checkout page.
  * 9.5 As a user, I can fill in my personal information, or have it auto-populated if it is already filled in on my profile.
  * 9.6 As a user I can view an order summary with a subtotal of all items in cart and which includes a calculated delivery charge.
  * 9.7 As a user I can easily enter my credit card payment information to make a purchase (#19).
  * 9.8 As a user on the checkout page, if I click 'Complete Order' and the transaction is unsuccessful for some reason, a message will be displayed.
  * 9.10 As a user who has completed a successful purchase, my order details will be summarised and displayed on my profile page (#21).
  * 9.11 As a user who has completed a successful purchase, I will receive a confirmation email (#22).
  * 9.12 As a user, I do not need to be logged in to make a purchase.
  * 9.13 As a user, I can easily view the total of my purchases at any time so that I can avoid spending too much (#5).
  * 9.14 As a user, I can feel my personal and payment information is safe and secure so that I can confidently provide the required information to make a purchase (#20).

**Feature 10. User Profile Page**

  * The profile page contains the user's information including their phone number, address and a list of their past orders.

Desktop profile page:

![User profile page](media/images/readme/profile-page-desktop.png)
  
Mobile profile page:

![Mbile profile page](media/images/readme/profile-page-mobile.png)
  
User stories relating to the user profile page:

  * 10.1 As a user, I can view my personal details on my profile page, including my name and address
  * 10.2 As a user, I can view my past orders on my profile page. 

**Feature 11. Admin CRUD pages for Products, Events and Blog**

  * The my account dropdown menu contains links to Product, Blog and Event Management pages. The Product Management page is the example chosen in the screenshots below, however Product, Blog and Event management CRUD features are all tested in the user testing section.
  * The Product Management Page contains the following fileds: Category, Sku, Name, Description, Has sizes, Price, Rating, Image url.
  * The Blog Management page contains the following fields: Title, Slug, Author, Content, Status.
  * The Events Management page contains the following fields: Title, Event category, Event date, Content, Status, Image.
  * All of the above pages contain the option to cancel or add/publish.
  * Products can be added/deleted from the all products page and product detail page.
  * Blog posts can be added/deleted from the blog post detail page.
  * Event posts can be added/deleted from the events list page.

Desktop product management page:

![Image of desktop product management page](media/images/readme/product-management-desktop-1.png)
![Image of desktop product management page](media/images/readme/product-management-desktop-2.png)

Mobile product management page:

![Image of mobile product management page](media/images/readme/product-management-mobile-1.png)
![Image of mobile product management page](media/images/readme/product-management-mobile-2.png)

User stories relating to the Product, Blog and Event Management pages:

  * 11.1 As an admin user, I can add products on the Product Managmenet page and receive confirmation when done (#23).
  * 11.2 As an admin user, I can add blog posts on the Blog Management page and receive confirmation when done (#34).
  * 11.3 As an admin user, I can add event posts on the Event Management page and receive confirmation when done (#37).
  * 11.4 As an admin user, I can edit and delete products on the all products and product detail pages and receive confirmation when done (#24 and #25).
  * 11.5 As an admin user, I can edit and delete Blog posts from the blog post detail page and receive confirmation when done (#35 and #36).
  * 11.6 As an admin user, I can edit and delete Event posts from the events list page and receive confirmation when done (#38 and #39).

**Feature 12. Admin**

  * A number of Admin views are configured at https://velo-city-rc.herokuapp.com/admin, through which the below user stories can be carried out. Full CRUD operations to the data in the database are available as well as search and filter options. These include Users, Blog posts, Event posts, Service bookings, Checkout orders, Products and Product categories.

Users:
![Image of admin user list](media/images/readme/admin-users.png)

Blog posts:
![Image of admin blog post list](media/images/readme/admin-blog-posts.png)

Event posts:
![Image of admin event posts list](media/images/readme/admin-event-posts.png) 

Service bookings:
![Image of admin service bookings list](media/images/readme/admin-service-bookings.png) 

Product categories
![Image of admin product categories list](media/images/readme/admin-product-categories.png) 

Products:
![Image of admin product list](media/images/readme/admin-products.png) 

Checkout orders:
![Image of admin checkout orders list](media/images/readme/admin-checkout-orders.png) 

User stories relating to Admin:

  * 12.1 As an admin user, I can view checkout orders in the Django admin page including the order number, date, full name, order total, delivery cost and grand total.
  * 12.2 As an admin user, I can view users in the Django admin page, including their username, email address,m first name, last name and staff status.
  * 12.3 As an admin user, I can view blog posts in the Django admin page, including title, slug, status, creation date and image.
  * 12.4 As an admin user, I can view event posts in the Django admin page, including title, status, creation date, image, event category and event date.
  * 12.5 As an admin user, I can view service bookings in the Django admin page, including user first name, last name, date requested and service type. 
  * 12.6 As an admin user, I can view product categories, their names and friendly names in the Django admin page.
  * 12.7 As an admin user, I can view products in the Django admin page, including their SKU, name, category, price, rating and image.

**Feature 13 Footer**

  * The Footer contains a link to Vélo City's Facebook for Business [marketing page](https://www.facebook.com/V%C3%A9lo-City-105357878885354).

  Vélo City Facebook for business page:
  ![Facebook page](media/images/readme/fb-desktop-1.png) 
  ![Facebook page](media/images/readme/fb-desktop-2.png) 
  ![Facebook page](media/images/readme/fb-desktop-3.png) 

  * There is also a link to Vélo City's Privacy and Refund & Returns Policies:
  
Desktop Privacy Policy:
![Privacy policy desktop](media/images/readme/privacy-desktop.png) 

Mobile Privacy Policy:
![Privacy policy mobile](media/images/readme/privacy-mobile.png) 

Desktop Refund Policy:
![Refund policy desktop](media/images/readme/refund-desktop.png) 

Mobile Refund Policy:
![Refund policy mobile](media/images/readme/refund-mobile.png) 

  * The footer also contains a Mailchimp marketing newsletter sign up form.

Email subscription sign up form desktop:
![Desktop footer](media/images/readme/footer-desktop-2.png) 

Email subscription sign up form mobile:
![Mobile footer](media/images/readme/footer-mobile-2.png) 

User Stories relating to the footer: 

  * 13.1 As a user, I can sign up to a Vélo City newsletter so that I can keep up to date with new products and offers (#27).
  * 13.2 As a user I can easily find information about the business, including contact information so that I can know more about the company I am buying from (#30).
  * 13.3 As a user, I can view the company's Privacy Policy so I feel like my privacy is protected while using the site and that the site is trustworthy.
  * 13.4 As a user, I can view and follow the company's Facebook for Business page so that I can stay up to date with news and offers (#41).
  * 13.5 As a user, I can view the company's return and refund policy so that I feel secure when making purchases on the site.


## Features to implement in future

  * An inventory management system so that the quantity of each product is entered when a product is added to the site, so that when all of the product's reserves have been purchased the product appears as no longer available on the site.
  * The blog posts could be linked to relevant products as a marketing strategy, e.g. a post on how to take up endurance cycling could be linked to the site's most popular endurance bike.
  * As the site developed, multiple images per product would be added.
  * The search feature will be expanded to allow a user to search by category.
  

# Technologies Used 

## Languages:

*  [HTML 5](https://en.wikipedia.org/wiki/HTML5)
*  [CSS 3](https://en.wikipedia.org/wiki/CSS)
*  [Javascript](https://www.javascript.com/)
*  [Django](https://www.djangoproject.com/)
*  [Python](https://www.python.org/)

    Python was used for the project's server side coding, in addition to a number of libraries. This is the list as per the requirements.txt file:

        asgiref==3.5.1
        boto3==1.24.2
        botocore==1.27.2
        dj-database-url==0.5.0
        Django==3.2
        django-allauth==0.41.0
        django-countries==7.2.1
        django-crispy-forms==1.14.0
        django-hvad==1.8.0
        django-libs==2.0.3
        django-storages==1.12.3
        gunicorn==20.1.0
        jmespath==1.0.0
        oauthlib==3.2.0
        Pillow==9.1.0
        psycopg2-binary==2.9.3
        python3-openid==3.2.0
        pytz==2022.1
        requests-oauthlib==1.3.1
        s3transfer==0.6.0
        sqlparse==0.4.2
        stripe==3.2.0

## Frameworks, libraries and programs used:

* [Balsamiq](https://balsamiq.com/) - to create wireframes for the site as part of the project preparation.
* [Google Fonts](https://fonts.google.com/) - to import the 'Bungee Shade' and 'Roboto Slab' fonts into the HTML file, which were then used throughout the site.
* [Font Awesome](https://fontawesome.com/) - for icons which were added to the footer.
* [Coolors](https://coolors.co/) - for an appropriate and attractive colour palette.
* [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - to inspect and debug the code through all stages of the development.
* [Lighthouse](https://developers.google.com/web/tools/lighthouse) - to check the site for performance, accessibility and best practices.
* [Am I Responsive](http://ami.responsivedesign.is/) - to produce a preview of the site on different devices.
* [W3C HTML Validator](https://validator.w3.org/#validate_by_input) - to validate HTML code.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - to validate CSS code.
* [GitHub](https://github.com/) - for hosting the project code and version control.
* [Gitpod](https://gitpod.io/account) - to write the code and push it to GitHub.
* [Github Pages](https://pages.github.com/) - to deploy the site.
* [Unsplash](https://unsplash.com/) - for images.
* [Pexels](https://pexels.com/) - for images.
* [Bootstrap](https://getbootstrap.com/docs/5.0) - for UI components across the website, e.g. buttons, navbar, cards.
* [Postgres](https://www.postgresql.org/) - the deployed project on Heroku uses a Postgres database.
* [SQLlite](https://www.sqlite.org/index.html) - The database used in local development was a SQLLite database.

# Deployment

There were a number of applications involved in the deployment of this site.

## Amazon Web Services

1. Create an account at aws.amazon.com.
2. Open the S3 application and create an S3 bucket named "velo-city-rc".

    ![AWS deployment step 1](media/images/readme/S3-1.png)

3. Enable ACLs and tick the "Block All Public access" setting.

    ![AWS deployment step 1](media/images/readme/S3-2.png)

4. Under the Properties section, turn on "Static Website Hosting", and set the index.html and the error.html values.

    ![AWS deployment step 2](media/images/readme/S3-3.png)

5. Under 'Permissions', paste in the following CORS configuration to set up the required access between Heroku and S3.

    ![AWS deployment step 3](media/images/readme/cors-configuration.png)

6. Click to edit the bucket policy and generate and set the below configuration:

    ![AWS deployment step 4](media/images/readme/S3-4.png)
    ![AWS deployment step 4](media/images/readme/S3-5.png)

7. Go to the Access Control List and set the List objects permission for everyone under the Public Access section.

    ![AWS deployment step 4](media/images/readme/S3-6.png)

8. Open the IAM application to control access to the bucket and set up a user group called manage-velo-city

     ![AWS deployment step 4](media/images/readme/S3-7.png)

9. Click on Policies, and Create Policy.

    ![AWS deployment step 4](media/images/readme/S3-8.png)

10. Click on the JSON tab and import a pre-built Amazon policy called AmazonS3FullAccess:

    ![AWS deployment step 4](media/images/readme/S3-9.png)

11. Set the following settings in the JSON tab:

    ![AWS deployment step 4](media/images/readme/S3-10.png)

12. Click Review Policy, give it a name and description and click Create Policy.

13. To attach the policy to the group, navigate to Groups, then Permissions, and under Add Permissions, select Attach Policy.

    ![AWS deployment step 4](media/images/readme/S3-11.png)

14. To create a user for the group, click Add User, and create one, e.g. 'velocity-staticfiles-user'.

    ![AWS deployment step 4](media/images/readme/S3-12.png)

15. Add the user to the group created earlier, making sure to download the CSV file which contains the user's access credentials.

16. Note the following AWS code in Settings.py. An environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage:

    ![AWS deployment Settings.py](media/images/readme/S3-14.png)

## Local Deployment

To run this project locally, clone the velo_city repository.

1. Login to GitHub (https://wwww.github.com) and select the repository rocrill/velo_city.

2. Click the 'Code' button and copy the HTTPS url, https://github.com/rocrill/velo_city.git.

3. In your IDE, run the command git clone https://github.com/rocrill/velo_city.git to clone the repository to your workspace.

4. Create an env.py file in your root directory and add the following:
import os
os.environ.setdefault("SECRET_KEY", TO BE ADDED BY USER)
os.environ.setdefault("DEVELOPMENT", '1')

5. Install the relevant packages as per the requirements.txt file.

6. In Settings.py set up a connection to either the local Sqllite database or the Heroku postgres database.

7. Add 'localhost' to the ALLOWED_HOSTS variable in Settings.py.

8. Run the following commands:
 * "python3 manage.py showmigrations" to check the status of the migrations.

 * "python3 manage.py migrate" to migrate the database.

 * "python3 manage.py createsuperuser" to create a super or admin user.

9. Start the application by running "python3 manage.py runserver".


## Heroku and Postgres

1. Create an account at heroku.com and create an app with a name in line with your repository, e.g. 'velo-city-rc'.
2. Under the Resources tab, add the Postgres database to the app.

    ![Heroku Deployment](media/images/readme/add-postgres.png)

The Postgres database url can be set as an environment variable in Heroku and your local env.py file.

3. Install dj-database-url and psycopg2-binary to your local environment and run pip3 freeze > requirements.txt to add them to the requirements.txt file.

4. Create a Procfile with the text: "web: gunicorn velo_city.wsgi:application".

5. In Settings.py set the connection to the Heroku Postgres database and set debug to false.

6. Ensure that Add 'localhost' and 'velo-city-rc.herokuapp.com' are added to the ALLOWED_HOSTS variable in Settings.py.

7. Run the following commands:

 * "python3 manage.py showmigrations" to check the status of the migrations.

 * "python3 manage.py migrate" to migrate the database.

 * "python3 manage.py createsuperuser" to create a super or admin user.

8. Install gunicorn and add it to the requirements.txt file using the command pip3 freeze > requirements.txt

9. From the CLI login to Heroku using the command `heroku login -i`.

10. Disable collectstatic in Heroku before any code is pushed.

11. Push the code to Heroku using the command `git push heroku main`.

12. Ensure the following environment variables are set in Heroku:

    ![Heroku Deployment](media/images/readme/config-vars.png)

13. Connect the Heroku app to GitHub, and enable automatic deploys.

14. Click deploy and once this is complete a link will be provided to access the application.


# Testing

The Vélo City site was regularly during the development process, by previewing it in the live server window and inspecting with Google Chrome DevTools at various stages.

When I was editing for responsiveness I tested the site on several different devices.

At the final stages of the project the W3C Markup Validator, W3C CSS Validator Services, along with PEP8 and JSHint were used to validate every page of the project to ensure there were no syntax errors.

## Testing User Stories

### General User Stories

* First Time Visitor Goals

  * As a First Time Visitor, I want to easily understand the purpose of the site.
  * As a First Time Visitor, I want to easily navigate throughout the site to find content.
  * As a First Time Visitor, I want to easily find information about the company.

  Result: Pass

  The site is clearly positioned as a cycling business with centrally placed navigation links to cycling products and blog and event posts. The 'About Us' page is also linked to the footer for further information. The navigation menu is set up so that navigation throughout the site is clear and straightforward.
 
* Returning Visitor Goals

  * As a Returning Visitor, I want to easily access and navigate to the different product links, my profile and the blog, event and booking pages.
  * As a Returning Visitor, I want to easily access the company's social media links so that I can follow them and keep up to date with news and offers.

  Result: Pass

  Product links, the blog, event and booking pages are all clearly marked in the navigation menu. The Account icon in the nav bar provides quick access to the user's profile and the company's social media page is easily accessed on the footer.
  
* Frequent User Goals

  * As a Frequent User, I want to be able to access the site from any device including mobile, even if I am on the go.

  Result: Pass

  The site is mobile optimised so that the design and functionality is as high quality on mobile as it is on desktop.

* Site Owner Goals

  * As a site owner, I want to create an a stylish and visually appealing website which elicits a positive emotional response in users.

  * As a site owner, I want to create easy to use website where products and their categories can be easily found and purchased.

  * As a site owner, I want to convey an impression of expertise on the sport of cycling and cycling products so that I can gain customer's trust and loyalty.

  * As a site owner, I want to have a good marketing strategy, including easily found social media links and a marketing email subscription option.

  Result: Pass

  The Vélo City site uses visually appealing styling including a classic font and sophisticated color palette. All products and categories can be accessed easily from teh navigation bar, and the business demonstrates expertise and trustworthiness through their blog content and transparent privacy and returns policies. There is a good marketing strategy in place, which includes a Facebook for Business page, Mailchimp newsletter sign up form and SEO optimised content throughout the site.

### Feature User Story Testing

**Feature 1. Navigation bar**

  * 1.1 As a user, I see the navigation bar with a logo on all pages and with a search box on a desktop, tablet and mobile.

    ![Desktop](media/images/readme/desktop-navbar.png)

    ![Mobile](media/images/readme/mobile-navbar.png)

    Result: Pass 

  * 1.2 As a user not logged in, I see a Register/Login link in the nav bar. Clicking this leads me to the registration or sign in pages and enables me to register or sign in (#6 and #7). 

    ![Desktop register/signin option when logged out](media/images/readme/signin-reg-1.png)
    ![Desktop reg page](media/images/readme/desktop-reg.png)
    ![Mobile reg page](media/images/readme/mobile-reg.png)
    ![Desktop sign in page](media/images/readme/desktop-signin.png)
    ![Mobile sign in page](media/images/readme/mobile-signin.png)

    Result: Pass

  * 1.3 As a logged in user, I am notified when I am logged in and I see a logout link in the nav which enables me to click sign out which logs me out.

    ![Login success message](media/images/readme/logout-option.png)
    ![Confirm logout](media/images/readme/confirm-logout.png)
    ![Logout success](media/images/readme/signout-success.png)

    Result: Pass

  * 1.4 As a user, I can easily receive email confirmation after registering so that I can verify that my account registration was successful (#9).

    ![Registration confirmation email](media/images/readme/reg-conf-email.png)
    ![Email confirmation success](media/images/readme/mail-confirmation-success.png)

    Result: Pass 

  * 1.5 As a user I can view the website logo in the header on desktop at all times, and a home link is present in the mobile nav menu at all times. Clicking these will bring me to the homepage.

    ![Desktop logo](media/images/readme/logo-present.png)
    ![Mobile home link](media/images/readme/home-link.png)

    Result: Pass

  * 1.6 As a user I can click the all product, service, blog and event nav links which bring me to the relevant pages.

    ![All products](media/images/readme/all-prod.png)
    ![Service Booking](media/images/readme/service-b.png)
    ![Blog](media/images/readme/blog.png)
    ![Events](media/images/readme/events.png)

    Result: Pass

  * 1.7 As a user if I encounter an error on the site, an applicable error message will be shown.

    Error messages are displayed for the following events on the site:

    (i) If a non-admin user attempts to create, edit or delete a product, blog or event post:

    ![non-admin crud attempt](media/images/readme/non-admin-crud-attempt.png)

    (ii) If a passed date is selected when submitting the date of a service booking:

    ![service date passed](media/images/readme/service-date-passed.png)

    (iii) If an invalid form is attempted to be submitted:

    ![Invalid form](media/images/readme/checkout-form-validation.png)

    (iv) If an unfound page is searched:

    ![page not found](media/images/readme/custom-404.png)

    The 500.html template has also been created so that a custom error page will be displayed to the user when a 500 error occurs.

    Result: Pass

  * 1.8 As a user, I can easily recover my password if I forget it so that I can easily get into the site if I forget my password without re-registering (#8).

    ![Reset password 1](media/images/readme/reset-p-1.png)
    ![Reset password 2](media/images/readme/reset-p-2.png)
    ![Reset password 3](media/images/readme/reset-p-3.png)
    ![Reset password 4](media/images/readme/reset-p-4.png)

  Result: Pass

  * 1.9 As a user, I can have a personalised user profile so that I can view my order history, order confirmations, saved favourite products and save my payment information(#10).

     ![User-profile](media/images/readme/user-profile.png)

    Result: Pass

  * 1.10 As a user, I can search for a product by name or description so that I can easily find specific products that I want to purchase (#14).

    ![User-profile](media/images/readme/user-profile.png)

  * 1.11 As a user, I can easily see what I've searched for and the number of results so that I can quickly decide if the product I want is available (#15).

    ![User-profile](media/images/readme/search-results-readme.png)

    Result: Pass

  * 1.12 As a user, I cannot access areas of the site that are restricted to admin users (e.g. product/blog/event management), and I receive an appropriate error message when I try to do so.

    Add/edit product:
    ![User-profile](media/images/readme/regular-user-error.png)

    Add/edit blog post:
    ![User-profile](media/images/readme/add-blog-regular.png)

    Add/edit event:
    ![User-profile](media/images/readme/add-event-regular.png)
  

**Feature 2. Home page**

  * 2.1 As a user, I want to see a homepage to contain a navigation bar and footer which clearly direct me to all available site pages.

    ![Desktop](media/images/readme/desktop1.png)
    ![Desktop](media/images/readme/desktop2.png)
    ![Mobile](media/images/readme/mob1.png)
    ![Mobile](media/images/readme/mob2.png)

    Result: Pass

  * 2.2 As a user, I want to see call to action button which directs me to the primary purpose of the site - to shop.

    ![Desktop](media/images/readme/desktop-calltoaction.png)
    ![Mobile](media/images/readme/mob-call-to-action.png)

    Result: Pass

**Feature 3. All Products page**

  * 3.1 As a user, I want to see a neatly displayed list of products with visually appealing images, clearly listing the name, price, category and rating of each product so I can decide on which products to view more detail on based on whether they are popular, relevant and within my price range (#1, #2, and #3).

    ![Desktop](media/images/readme/all-prod-desktop.png)
    ![Mobile](media/images/readme/all-prod-mobile.png)

    Result: Pass

  * 3.2 As a user if there are more than 8 products on the page, the page is paginated in order to maintain the neat look of the site and to avoid endless scrolling for the user.

    ![Desktop](media/images/readme/desktop-pagination1.png)
    ![Desktop](media/images/readme/desktop-pagination2.png)
    ![Mobile](media/images/readme/mobile-pagination.png)

    Result: Pass

  * 3.3 As a user, I want to quickly identify offers and deals so that I can get the best value (#4).

    The website currently only has one discount offer available, which is for free delivery on orders over 50 euro. This is displayed prominently on both desktop and mobile:

    ![Desktop](media/images/readme/deliverybanner-desktop.png)
    ![Mobile](media/images/readme/deliverybanner-mobile.png)

    Result: Pass

  * 3.4 As an admin, I want to be able to edit or delete products from the all products page.

    ![Desktop](media/images/readme/all-prod-editdelete.png)
    ![Mobile](media/images/readme/mob-editdelete.png)

    Result: Pass

  * 3.5 As a user, I can sort the list of available products so that I can easily identify the best value, best rated and categorically sorted products (#11).

    ![Sorting options](media/images/readme/sortoptions.png)
    ![Sorting example: price low to high](media/images/readme/sort-eg-lowhigh.png)

    Result: Pass

  * 3.6 As a user, I can sort a specific category of product so that I can find the best-priced or best-rated product in a specific category, or sort by name in that category (#12).

    ![Desktop](media/images/readme/category-sorted.png)

    Result: Pass

  * 3.7 As a user, I can sort multiple categories of products simultaneously so that I can find the best-priced or best-rated products across broad categories, such as "clothing" and "bikes" (#13).

    ![Desktop](media/images/readme/multiple-categories-price-lowhigh.png)
  
    Result: Pass

**Feature 4. Category-specific product page**

  * 4.1 As a user, I want to be able to easily access a catergory-specific product page so that I can access the content that I am interested in quickly and easily.

    ![Desktop](media/images/readme/category-sorted.png)

    Result: Pass

**Feature 5. Product detail page**

  * 5.1 As an admin user, I want to be able to edit or delete a product from the detail page so that I can easily edit products as an admin.

    ![Desktop](media/images/readme/prod-detail-editdelete.png)

    Result: Pass

  * 5.2 As a user, I want to be able to view all product information on the product detail page including an image, price, rating, category, description and size.

    ![Desktop](media/images/readme/prod-detail.png)

    Result: Pass

  * 5.3 As a user, I want to be able to view a size chart for the product I am interested in so that I can be sure I am selecting the correct size for myself (#40).

    ![Desktop](media/images/readme/size-guide.png)
    ![Desktop](media/images/readme/size-guide-2.png)

    Result: Pass

  * 5.4 As a user, I want to be able to select the quantity of items I want and put a product in my shopping cart directly from the product detail page so that I can shop efficiently (#16).

    ![Desktop](media/images/readme/quantity-addtocart.png)
    ![Desktop](media/images/readme/quantity-addtocart-2.png)

    Result: Pass

  * 5.5 As a user, I can see similar/recommended items so that I can enjoy a personalised shopping experience and be aware of the products I am most likely to like and purchase (#28).  

    ![Desktop](media/images/readme/recommended-products.png)

    Result: Pass

**Feature 6. Service Booking page**

  * 6.1 As an user, I want to be able to book a bike service easily and efficiently, so that I can arrange to resolve an issue with my bike quickly and easily (#26).

    ![Service booking](media/images/readme/book-service-1.png)

    Result: Pass

  * 6.2 As a user, I want to receive a confirmation message so I know that I have successfully submitted my booking form.

    ![Service booking](media/images/readme/book-service-2.png)

    Result: Pass

  * 6.3 As a user, I want to receive a notification if I have accidentally selected a booking date in the past so I know that I need to fill out the form again.

    ![Service booking](media/images/readme/service-date-passed.png)

    Result: Pass

**Feature 7. Blog**
  
  * 7.1 As an user, I want to be able to access blog content with cycling tips and guides so that I can improve my knowledge of cycling and become a better cyclist (#31).

    ![Blog post list](media/images/readme/blog-postlist-desktop-1.png)
    ![Blog post list](media/images/readme/blog-postlist-desktop-2.png)
    ![Blog post detail](media/images/readme/blog-postdetail-desktop-1.png)
    ![Blog post detail](media/images/readme/blog-postdetail-desktop-2.png)

    Result: Pass

**Feature 8. Events Page**

  * 8.1 As a user, I want to see a list of upcoming Irish cycling events in order of event date so that I can engage with the cycling community and potentially take part in competitive events (#33).

    ![Events List](media/images/readme/event-list-desktop.png)

    Result: Pass

  * 8.2 As a user, I want to be able to filter the cycling events for categories that are relevant to me.

    ![Events List](media/images/readme/events-category-filter.png)

    Result: Pass

**Feature 9. Shopping Cart and Checkout**

  * 9.1 As a user, I can click on a product, select a size and quantity and add it to my bag (receiving a notification when I've done so) in order to purchase it. 

    ![Checkout process](media/images/readme/desktop-checkout-process-1.png)

    Result: Pass

  * 9.2 As a user, I can click on the cart icon and be brought to my bag to see the contents in order to know what I have selected so far and the subtotal. If no contents are there, I will see a message that the cart is empty (#17).

    ![Checkout process](media/images/readme/desktop-checkout-process-1.png)
    ![Checkout process - empty cart](media/images/readme/empty-cart.png)

    Result: Pass

  * 9.3 As a user, I can update the quantity or remove an item from my shopping bag (#18).

    (i)![Checkout process - cart](media/images/readme/cart.png)
    (ii)![Checkout process - adjusted](media/images/readme/adjusted-cart.png)

    Result: Pass 

  * 9.4 As a user, I can click on the Secure Checkout button on the cart page or toast message, and will be directed to the checkout page.
  * 9.5 As a user, I can fill in my personal information, or have it auto-populated if it is already filled in on my profile.

    (i)![Checkout process - adjusted](media/images/readme/secure-checkout-1.png)
    (ii)![Checkout process - adjusted](media/images/readme/secure-checkout-1.png)

    Result: Pass
  
  * 9.6 As a user I can view an order summary with a subtotal of all items in cart and which includes a calculated delivery charge.

    ![Checkout process - adjusted](media/images/readme/order-summary.png)

    Result: Pass

  * 9.7 As a user I can easily enter my credit card payment information to make a purchase (#19).

    ![Checkout process - card info](media/images/readme/enter-card-info.png)

    Result: Pass

  * 9.8 As a user on the checkout page, if I click 'Complete Order' and the transaction is unsuccessful for some reason, a message will be displayed.

    ![Checkout process - unsuccessful transaction](media/images/readme/unsuccessful-transaction.png)

    Result: Pass

  * 9.10 As a user who has completed a successful purchase, my order details will be summarised and displayed on my profile page (#21).

    (i)![Checkout process - summary](media/images/readme/order-summary-confirmation.png)
    (ii)![Checkout process - summary profile](media/images/readme/order-summary-profile.png)

    Result: Pass

  * 9.11 As a user who has completed a successful purchase, I will receive a confirmation email (#22).

    ![Checkout process - email confirmation](media/images/readme/order-email-confirmation.png)

    Result: Pass

  * 9.12 As a user, I do not need to be logged in to make a purchase.

    (i)![Checkout process - logged out purchase](media/images/readme/loggedout-order-1.png)
    (ii)![Checkout process - logged out purchase](media/images/readme/loggedout-order-2.png)

    Result: Pass

  * 9.13 As a user, I can easily view the total of my purchases at any time so that I can avoid spending too much (#5).

    The cart total is visible and up to date at all times on the header of the page:
    ![Checkout process - cart total visible](media/images/readme/cart-total-visible.png)

    Result: Pass

  * 9.14 As a user, I can feel my personal and payment information is safe and secure so that I can confidently provide the required information to make a purchase (#20).

    Users are invited to make a secure checkout where they are given an extra notification that their card will be charged. Once submitted the payment details are passed through Stripe's secure overlay.
    
    ![Checkout process - input payment details](media/images/readme/enter-card-info.png)
    ![Checkout process - stripe overlay](media/images/readme/overlay.png)

    Result: Pass

**Feature 10. User Profile page**

* 10.1 As a user, I can view my personal details on my profile page, including my name and address
* 10.2 As a user, I can view my past orders on my profile page. 

  ![User profile](media/images/readme/profile-page-desktop.png)

  Result: Pass


**Feature 11. Admin CRUD pages for Products, Events and Blog**

* 11.1 As an admin user, I can add products on the Product Managmenet page and receive confirmation when done (#23).

  (i)![Admin add product](media/images/readme/admin-add-product-view.png)
  (ii)![Admin add product](media/images/readme/admin-addproduct-2.png)

  Result: Pass

* 11.2 As an admin user, I can add blog posts on the Blog Management page and receive confirmation when done (#34).

  (i)![Admin add blog post](media/images/readme/admin-addblogpost-1.png)
  (ii)![Admin add blog post](media/images/readme/admin-addblogpost-2.png)

  Result: Pass

* 11.3 As an admin user, I can add event posts on the Event Management page and receive confirmation when done (#37).

  ![Admin add event post](media/images/readme/admin-addevent.png)

  Result: Pass

* 11.4 As an admin user, I can edit and delete products on the all products and product detail pages and receive confirmation when done (#24 and #25).

  (i)![Admin edit product](media/images/readme/admin-edit-product.png)
  (ii)![Admin edit product](media/images/readme/admin-edit-product-2.png)
  (ii)![Admin delete product](media/images/readme/admin-delete-product.png)

  Result: Pass

* 11.5 As an admin user, I can edit and delete Blog posts from the blog post detail page and receive confirmation when done (#35 and #36).

  ![Admin blog edit](media/images/readme/edit-blogpost.png)
  ![Admin blog delete](media/images/readme/delete-blogpost.png)

  Result: Pass

* 11.6 As an admin user, I can edit and delete Event posts from the events list page and receive confirmation when done (#38 and #39).

  ![Admin edit event](media/images/readme/admin-edit-event.png)
  ![Admin delete event](media/images/readme/admin-delete-event.png)

  Result: Pass

**Feature 12. Admin**

User stories relating to Admin:

  * 12.1 As an admin user, I can view checkout orders in the Django admin page including the order number, date, full name, order total, delivery cost and grand total.

    ![Admin checkout orders](media/images/readme/admin-checkout-orders-2.png)

    Result: Pass

  * 12.2 As an admin user, I can view users in the Django admin page, including their username, email address, first name, last name and staff status.

    ![Admin users](media/images/readme/admin-users.png)

    Result: Pass

  * 12.3 As an admin user, I can view blog posts in the Django admin page, including title, slug, status, creation date and image.

    ![Admin blog posts](media/images/readme/admin-blog-posts.png)

    Result: Pass

  * 12.4 As an admin user, I can view event posts in the Django admin page, including title, status, creation date, image, event category and event date.

    ![Admin events](media/images/readme/admin-event-posts.png)

    Result: Pass

  * 12.5 As an admin user, I can view service bookings in the Django admin page, including user first name, last name, date requested and service type. 

    ![Admin service bookings](media/images/readme/admin-service-bookings.png)

    Result: Pass

  * 12.6 As an admin user, I can view product categories, their names and friendly names in the Django admin page.

    ![Admin product categories](media/images/readme/admin-product-categories.png)

    Result: Pass

  * 12.7 As an admin user, I can view products in the Django admin page, including their SKU, name, category, price, rating and image.

    ![Admin Products](media/images/readme/admin-products.png)

    Result: Pass

**Feature 13. Footer**

  * 13.1 As a user, I can sign up to a Vélo City Mailchimp newsletter so that I can keep up to date with new products and offers (#27).

    (i)![Mailchimp form](media/images/readme/signup-mailchimp.png)
    (ii)![Mailchimp form](media/images/readme/useradded-MC-campaign.png)

    Result: Pass

  * 13.2 As a user I can easily find information about the business, including contact information so that I can know more about the company I am buying from (#30).

    ![About business](media/images/readme/aboutus-1.png)
    ![About business](media/images/readme/aboutus-2.png)

    Result: Pass

  * 13.3 As a user, I can view the company's Privacy Policy so I feel like my privacy is protected while using the site and that the site is trustworthy.

    ![Privacy policy](media/images/readme/privacy-1.png)
    ![Privacy policy](media/images/readme/privacy-2.png)

    Result: Pass

  * 13.4 As a user, I can view and follow the company's Facebook for Business page so that I can stay up to date with news and offers (#41).

    ![FB Page](media/images/readme/fb-1.png)
    ![FB Page](media/images/readme/fb-desktop-1.png)
    ![FB Page](media/images/readme/fb-desktop-2.png)

    Result: Pass

  * 13.5 As a user, I can view the company's return and refund policy so that I feel secure when making purchases on the site.

    ![Returns](media/images/readme/returns-link.png)
    ![Returns](media/images/readme/returns-desktop.png)

    Result: Pass

## Validator Testing

* The following HTML Validator Errors & Warnings were raised as part of the testing process.

1. Checkout page errors:
![Checkout errors](media/images/readme/checkout-page-errors.png)

    Comment:
    There are several HTML validation errors and warnings on the Checkout page which can be seen below. These are a result of a fix that was implemented to correct an issue with the decrement and increment quantity buttons whereby they did not work correctly on a large screen device. This issue was flagged during the Boutique Ado walkthrough project. I would have tried to address this issue if I had more time, however it did not seem possible without re-writing the code from scratch at a late stage of the project.

2. Event page error:
![Event page error](media/images/readme/event-page-error.png)

    Fix: Replace the `h2`-wrapped event post headings with `span`-wrapped headings including in-line styling to increase the font size.

3. Loading overlay error:
![Overlay error](media/images/readme/loading-overlay-error.png)

    Comment:
    This `h1` is empty as it is intended to contain an overlay icon only. This is part of the Stripe code.

4. Add Product/Blog/Event post error:
![Add post error](media/images/readme/add-product-blog-event-error.png)

    Comment:
    These errors have been raised by code from Django and so cannot be accessed to address.

## PEP8

The [AutoPEP8](https://unsplash.com/photos/RKU4zSFitWM) tool was used to bring all Python code to PEP8 standard.

## JSHint

All Javascript was run through the JSHint validator and no errors were returned.

## Lighthouse Testing

The Lighthouse report from Google Chrome DevTools showed good results for performance and accessibility of the site, particularly on desktop devices.

Home page:
![Desktop](media/images/readme/LH-desktop-home.png)
![Mobile](media/images/readme/LH-homepage-mobile.png)

All Products page:
![Desktop](media/images/readme/LH-Allproducts-desktop.png)
![Mobile](media/images/readme/LH-ALLPRODUCTS-MOBILE.png)

Product detail page:
![Desktop](media/images/readme/LH-desktop-productdetail-page.png)
![Mobile](media/images/readme/LH-mobile-productdetail-page.png)

Service Booking page:
![Desktop](media/images/readme/LH-desktop-booking.png)
![Mobile](media/images/readme/lh-mobile-booking.png)

Blog:
![Desktop](media/images/readme/LH-blog-desktop.png)
![Mobile](media/images/readme/LHblog-mobile.png)

Events:
![Desktop](media/images/readme/LH-desktop-events.png)
![Mobile](media/images/readme/LH-events-mobile.png)

Checkout:
![Desktop](media/images/readme/LH-desktop-checkout.png)
![Mobile](media/images/readme/LH-mobile-checkout.png)

Shopping Cart:
![Desktop](media/images/readme/LH-desktop-shoppingcart.png)
![Mobile](media/images/readme/LH-mobile-shoppingcart.png)

## Further Testing

* Devices and browsers:

  * The Website was tested on multiple browsers - Google Chrome, Safari, Microsoft Edge and Firefox browsers.
  * The website was viewed on all devices available to me - Desktop, Laptop, iPhone13 Mini, and Oppo Find X2 Lite.

* Site Features:

  * The nav bar remains and the top of the page and the menu items adapt to remain within the nav bar on all devices.
  * The font is legible on all device sizes.
  * Images are resized where needed and never stretched or distorted on smaller devices.
  * All buttons and links direct to the correct parts of the site.

## Bugs

* Fixed:

  * There was initially an error with the increment and decrement item buttons on the checkout page. The increment button went beyond it's intended upper limit above 99, and the decrement button went below it's lower limit of 1. To resolve this, the Javascript code was updated so that it all quantity fields present on the page would be updated, rather than quantity fields targeted by id only. Note the functionality was fixed, however it raised validation errors as documented above.
  
* Known:

  * There are no known bugs at present.

# Credits

## Code

The Code Institute LMS content, including the Django Boutique Ado walkthrough project, as well as some posts on Stackoverflow were used to create this site. All code taken from these resources has been adapted to suit the needs of this site, except for the specific cases referenced below.

The Bootstrap footer was taken from [Bootstrap](https://mdbootstrap.com/snippets/standard/mdbootstrap/2885103?view=side).

This YouTube [video]() was used when building out the view to delete a recipe post from the front end of the site.

This Stackoverflow [article](https://stackoverflow.com/questions/50439356/django-date-validation-help-needed) was used when applying date valifdation to the service booking form. 

This Stackoverflow [article](https://stackoverflow.com/questions/45379727/make-images-the-same-size-in-bootstrap-grid) was used to make all product images o the All Products page the same size.

This Django [article](https://forum.djangoproject.com/t/how-to-set-data-calendar-widget-for-datefield-and-datetimefield-wiht-format-day-month-year-dd-mm-yyyy/7243) was used when implementing a date and time field to the add Event form.

This Stackoverflow [article](https://stackoverflow.com/questions/22800804/display-static-page-in-django) was used when looking for a simple solution for content-sparse static pages e.g. About us, Contact us, Privacy Policy and Refunds and Returns.

This Stackoverflow [article](https://stackoverflow.com/questions/10872405/django-allow-user-to-submit-valid-html-in-form-field) was used when text needed to be styled or modified via the front end crud form in order to be displayed appropriately as a blog post, e.g. large text for title.

This Stackoverflow [article](https://stackoverflow.com/questions/10872405/django-allow-user-to-submit-valid-html-in-form-field) was used when text needed to be styled on modified on via the front end crud form in order to be displayed appropriately as a blog post, e.g. large text for title.

This Django [article](https://docs.djangoproject.com/en/4.0/topics/pagination/) was used when setting up pagination on the site.

## Content

Content for the blog post on how to descend safely was taken from the Liv Cycling [website](https://www.liv-cycling.com/global/campaigns/how-to-descend-on-a-road-bike/21996)

Content for the blog post on how to corner was taken from the Liv Cycling [website](https://www.liv-cycling.com/global/campaigns/how-to-corner-on-a-road-bike/21772)

Background on the B2C business model was found on this [website](https://www.tutorialspoint.com/e_commerce/e_commerce_b2c_mode.htm)

## Images

All images were sourced from Unsplash and Pexels:

Bike image by David Jones on [Unsplash](https://unsplash.com/photos/IYU2eCw9iek)

Bike image by Metin Ozer on [Unsplash](https://unsplash.com/photos/2hwowscdWLA)

Bike image by Nik Owens on [Unsplash](https://unsplash.com/photos/RKU4zSFitWM)

Bike image by Rayyu Maldives on [Unsplash](https://unsplash.com/photos/i-rETD5k1Qk)

Bike image by Dmitrii Vaccinium on [Unsplash](https://unsplash.com/photos/sw9Vozf6j_4)

Bike image by Mikkel Bech on [Unsplash](https://unsplash.com/photos/yjAFnkLtKY0)

Cycling jersey image by Ashley de Lotz on [Unsplash](https://unsplash.com/photos/xhHutIhi-u0)

Cycling jersey image by Munbaik Cycling Clothing on [Unsplash](https://unsplash.com/photos/JyBUMdyWk8E)

Cycling jersey image by Rehook Bike on [Pexels](https://www.pexels.com/photo/close-up-of-fixing-a-bicycle-10263877/)

Woman cyclist image by Bono Tsang on [Pexels](https://www.pexels.com/photo/a-woman-riding-a-bicycle-8056390/)

Men's cycle race image by Pixabay on [Pexels](https://www.pexels.com/photo/high-angle-view-of-people-on-bicycle-248547/)

Endurance cyclist image by alexandre saraiva carniato on [Pexels](https://www.pexels.com/photo/man-riding-a-red-road-bike-5970279/)

Bike image by Maria Orlova on [Pexels](https://www.pexels.com/photo/bicycle-parked-on-town-street-covered-with-fallen-autumn-leaves-4916477/)

Bike image by Adam Dubec on [Pexels](https://www.pexels.com/photo/gray-commuter-bike-parked-on-road-beside-sea-1595483/)

Bike image by Alain Frechette on [Pexels](https://www.pexels.com/photo/pink-beach-cruiser-bicycle-near-wall-1431117/)

Bike image by Philipp M on [Pexels](https://www.pexels.com/photo/black-and-white-hardtail-bike-on-brown-road-between-trees-100582/)

Bike image by Philipp M on [Pexels](https://www.pexels.com/photo/black-and-white-hardtail-bike-on-brown-road-between-trees-100582/)

Coffee morning event image by Pixabay on [Pexels](https://www.pexels.com/photo/beverage-blue-book-breakfast-531829/)

Two female cyclists image by Coen van de Broek on [Unsplash](https://unsplash.com/photos/OFyh9TpMyM8)

Sprinting cyclist image by Pixabay on [Pexels](https://www.pexels.com/photo/person-riding-road-bike-on-the-road-38296/)

Ladies cycling shorts image by Los Muertos Crew on [Pexels](https://www.pexels.com/photo/fit-woman-stretching-next-to-railing-10042872/)

Mens cycling shorts image by Carissa Rogers on [Pexels](https://www.pexels.com/photo/photo-of-person-riding-bicycle-1504207/)

Mens cycling shorts image by Carissa Rogers on [Pexels](https://www.pexels.com/photo/photo-of-person-riding-bicycle-1504207/)

Bike image by Kimsanxw on [Pexels](https://www.pexels.com/photo/bicycle-parked-beside-a-indoor-plant-10410451/)

Bike image by Tiffany Nutt on [Unsplash](https://unsplash.com/photos/0ClfreiNppM)

Image of women's cycling kit by Coen van de Broek on [Unsplash](https://unsplash.com/photos/hdyYvZ3Hj7w)

Image of men's base layer by Munbaik Cycling Clothing on [Pexels](cyclist-near-unrecognizable-friend-riding-bikes-on-road-5851037/)

Image of woman's base layer by Yan Krukov on [Unsplash](https://www.pexels.com/photo/dancing-young-woman-in-white-crop-tank-top-and-blue-cycling-shorts-7312372/)

Image of black bike by Mikkel Bech on [Unsplash](https://unsplash.com/photos/yjAFnkLtKY0)

Image of Giant bike by Alexa Diffor on [Unsplash](https://unsplash.com/photos/z-hKDdfYMn4)

Image of bike by @mustachescactus on [Unsplash](https://unsplash.com/photos/vZAk_n9Plfc)


# Acknowledgements

I would like to thank my course facilitator Richard Wells and my fellow CI classmates for their help and support throughout the course.