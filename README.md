 # Flask Todo Webapp with SQLAlchemy

This is a simple Flask web application that provides a basic todo list functionality. The application uses SQLAlchemy to interact with a SQLite database in the back end. The application can be run locally or using Docker.

## Requirements

If running the application locally, the following software is required:

- Python 3.x
- Flask
- SQLAlchemy

If running the application using Docker, Docker and Docker Compose are required.

The application has been developed and tested on Windows 10 using Python 3.8. It may work on other platforms and Python versions, but this has not been tested.

### Running Locally

To install and run the application locally, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal or command prompt and navigate to the repository directory.
3. Create a virtual environment for the application by running `python -m venv venv`.
4. Activate the virtual environment by running `venv\Scripts\activate` on Windows or `source venv/bin/activate` on Linux/Mac.
5. Install the required Python packages by running `pip install -r requirements.txt`.
6. Start the application by running `python app.py`.

The application will be available at `http://localhost:5000` in your web browser.

### Running with Docker

To install and run the application using Docker, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal or command prompt and navigate to the repository directory.
3. Build the Docker image by running `docker build`
4. Start the Docker container by running `docker-compose up`.

The application will be available at `http://localhost:5000` in your web browser.

## Usage

The home page of the application displays the current todo list, which is initially empty. You can add a new task to the todo list by entering a task description in the input field and clicking the "Add Task" button.

You can mark a task as completed by clicking the checkbox next to its description. Completed tasks are displayed with a strike-through effect.

You can delete a task by clicking the "Delete" button next to its description.



## License

This application is licensed under the MIT License. See the `LICENSE` file for details.
