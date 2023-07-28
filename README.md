# Salary Visualization

This is a data visualization app for salary data in the Data Science field. It provides interactive charts and visualizations based on a large CSV file containing salary data. The app is built with NextJS and Recharts for the frontend, and Python FastAPI with ElasticSearch for the backend.

## Features

- Visualize salary data using various chart types, including bar charts, line charts, and grouped bar charts.
- Filter and explore salary data based on different criteria such as job title, company size, and location.
- Retrieve salary data from a ElasticSearch database and display it in a user-friendly and visually appealing manner.

## Technologies Used

- Frontend: NextJS, Recharts, Sass.
- Backend: Python, FastAPI, ElasticSearch.

## Running the Application

### Local Environment

To run the application locally, you will need to have the following environment variable set:

- `ES_HOST=http://localhost:9200`: This environment variable specifies the ElasticSearch URL when running the FastAPI Server locally.

- Change directory to the backend directory.

- Launch the Docker Compose with the necessary services:

```
docker compose up elasticsearch kibana -d
```

- Start the app locally:

```
python -m uvicorn main:app --reload
```

### Docker Environment

When running the application with Docker, you will need to configure the Docker Compose file with the following environment variable:

```
services:
    fastapi:
        environment:
            - "ELASTICSEARCH_URL=http://elasticsearch:9200"
```

This environment variable specifies the ElasticSearch URL when running the FastAPI Server within the Docker environment.

- Launch all services with Docker Compose.

```
docker compose up -d
```
