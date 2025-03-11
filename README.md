# Flutter Chat App Backend

This is the backend for a Flutter-based chat application, built using Python.

## Features

- User authentication (Signup/Login)
- Real-time messaging
- Database integration
- Secure API endpoints

## Requirements

Make sure you have the following installed:

- Python 3.x
- pip
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Satyam1Vishwakarma/flutter-chatapp-backend.py.git
   cd flutter-chatapp-backend.py
   ```

2. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the server:

```sh
python app.py
```

## API Endpoints

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| POST   | /register     | Register a new user |
| POST   | /login        | Authenticate user   |
| GET    | /messages     | Fetch chat messages |
| POST   | /send-message | Send a new message  |

## Deployment

You can deploy the backend using services like:

- Heroku
- AWS
- DigitalOcean
- Render

## Contributing

Feel free to submit pull requests to improve this project.
