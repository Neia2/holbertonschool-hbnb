# holbertonschool-hbnb

Holberton School HBNB Project

# Holberton School HBNB Project

## Description

This project is a Flask-based web application that provides API endpoints for managing places, cities, amenities, and users. It utilizes SQLAlchemy for database management and Flask-Restx for building RESTful APIs.

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

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

Collabotareus: Benjamin Jakob, Neia Nascimento and Soufian Mratz.
