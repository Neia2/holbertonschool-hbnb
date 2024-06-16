# holbertonschool-hbnb

Holberton School HBNB Project

# HBnB Evolution Project: Part 1 Guide
Welcome to the first leg of our exciting journey - creating our very own web application, HBnB Evolution, modeled after AirBnB using Python and Flask!

## What’s Cooking in Part 1?

# Sketching with UML

You’ll kick things off by drawing out the backbone of our application using UML (Unified Modeling Language). Think of it like creating the architectural blueprint for a building. It’s where you decide how your classes and components will interact.

# Testing Our Logic

After setting up our blueprint, it’s time to make sure everything works as planned. You’ll create tests for the API and business logic. It’s like making sure all the gears turn smoothly in a machine.

# Building the API
Now, for the real deal - implementing the API. This is where your blueprint comes to life. You’ll use Flask to create an API that plays well with our business logic and file-based persistence (for now).

# File-Based Data Storage
We’re starting simple with a file-based system for storing our data. Choose your format – text, JSON, XML – you name it. Keep in mind that we’ll shift to a database later, so build it smart!

# Packaging with Docker
Finally, you’ll wrap everything up in a neat Docker image. It’s like packing your app in a container that can be easily moved and deployed anywhere.


The project is organized into the following directories and files:


holbertonschool-hbnb/
├── api/
│ ├── init.py
│ ├── app.py
│ └── country_city_routes.py
├── models/
│ ├── init.py
│ ├── city.py
│ ├── country.py
│ └── countries_data.py
├── persistence/
│ ├── init.py
│ ├── data_manager.py
│ └── data.json
├── README.md
└── requirements.txt


- `api/`: Contains the Flask application and routes.
- `models/`: Contains the data models for countries and cities.
- `persistence/`: Contains the data manager for saving and retrieving data.
- `README.md`: The readme file for the project.
- `requirements.txt`: Lists the Python dependencies for the project.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/holbertonschool-hbnb.git
    cd holbertonschool-hbnb
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set the FLASK_APP environment variable**:
    ```sh
    export FLASK_APP=api.app
    ```

5. **Run the Flask application**:
    ```sh
    flask run
    ```

## Usage

After starting the Flask application, you can access the API at `http://127.0.0.1:5000/api`. Use tools like `curl`, Postman, or a web browser to interact with the API.

## API Endpoints

### Country Endpoints

- **Get all countries**: 
    ```sh
    GET /api/countries/
    ```

- **Get a specific country by code**: 
    ```sh
    GET /api/countries/<country_code>
    ```

- **Get cities in a specific country**: 
    ```sh
    GET /api/countries/<country_code>/cities
    ```

### City Endpoints

- **Add a new city**:
    ```sh
    POST /api/cities/
    ```

    **Request Body**:
    ```json
    {
        "name": "City Name",
        "country_code": "Country Code"
    }
    ```

- **Get all cities**: 
    ```sh
    GET /api/cities/
    ```

- **Get a specific city by ID**: 
    ```sh
    GET /api/cities/<city_id>
    ```

- **Update a city by ID**: 
    ```sh
    PUT /api/cities/<city_id>
    ```

    **Request Body**:
    ```json
    {
        "name": "New City Name",
        "country_code": "Country Code"
    }
    ```

- **Delete a city by ID**: 
    ```sh
    DELETE /api/cities/<city_id>
    ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Create a pull request.


---------------------------------------------------------------------------------------------------------------------------------------

Collaborators: Benjamin Jakob, Neia Nascimento and Soufian Mgratz.
