# HBnB Evolution Project: Part 1 Guide

Welcome to the first leg of our exciting journey - creating our very own web application, HBnB Evolution, modeled after AirBnB using Python and Flask!

## What’s Cooking in Part 1?

### Sketching with UML
You’ll kick things off by drawing out the backbone of our application using UML (Unified Modeling Language). Think of it like creating the architectural blueprint for a building. It’s where you decide how your classes and components will interact.

### Testing Our Logic
After setting up our blueprint, it’s time to make sure everything works as planned. You’ll create tests for the API and business logic. It’s like making sure all the gears turn smoothly in a machine.

### Building the API
Now, for the real deal - implementing the API. This is where your blueprint comes to life. You’ll use Flask to create an API that plays well with our business logic and file-based persistence (for now).

### File-Based Data Storage
We’re starting simple with a file-based system for storing our data. Choose your format – text, JSON, XML – you name it. Keep in mind that we’ll shift to a database later, so build it smart!

### Packaging with Docker
Finally, you’ll wrap everything up in a neat Docker image. It’s like packing your app in a container that can be easily moved and deployed anywhere.

## The Three Layers of Our API Cake

- **Services Layer:** This is where our API greets the world. It handles all the requests and responses.
- **Business Logic Layer:** The brain of the operation. This is where all the processing and decision-making happens.
- **Persistence Layer:** For now, it’s our humble file system, but we’ll graduate to a database in the future.

## The Data Model: Key Entities

### Places
These are the heart of our app. Each place (like a house, apartment, or room) has characteristics like name, description, address, city, latitude, longitude, host, number of rooms, bathrooms, price per night, max guests, amenities, and reviews.

### Users
Users are either owners (hosts) or reviewers (commenters) of places. They have attributes like email, password, first name, and last name. A user can be a host for multiple places and can also write reviews for places they don’t own.

### Reviews
Represent user feedback and ratings for a place. This is where users share their experiences.

### Amenities
These are features of places, like Wi-Fi, pools, etc. Users can pick from a catalog or add new ones.

### Country and City
Every place is tied to a city, and each city belongs to a country. This is important for categorizing and searching places.

## Business Logic: Rules to Live By

- **Unique Users:** Each user is unique and identified by their email.
- **One Host per Place:** Every place must have exactly one host.
- **Flexible Hosting:** A user can host multiple places or none at all.
- **Open Reviewing:** Users can write reviews for places they don’t own.
- **Amenity Options:** Places can have multiple amenities from a catalog, and users can add new ones.
- **City-Country Structure:** A place belongs to a city, cities belong to countries, and a country can have multiple cities.

## Why These Attributes Matter?

- **Uniqueness:** The UUID4 ensures that each entity is distinct, eliminating any confusion or overlap, especially crucial when we scale up.
- **Traceability:** With created_at and updated_at, we can track the lifecycle of each entity, which is invaluable for debugging, auditing, and understanding user interactions over time.

When designing your classes and database schemas (in the later stages), make sure these attributes are included as a standard part of every entity.

- Utilize Python’s `uuid` module to generate UUID4 ids.
- Leverage Python’s `datetime` module to record timestamps for creation and updates.

![UML](/root/holbertonschool-higher_level_programming/holbertonschool-hbnb/uml.png)
