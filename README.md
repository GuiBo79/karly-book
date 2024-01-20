# Fire Incidents Application

## Overview
This application is designed to manage and analyze fire incident data from https://data.sfgov.org/ . It uses a Python script to load data into a MySQL database and provides an interface through phpMyAdmin for data visualization, management and reporting.

## Prerequisites
- Docker
- Docker Compose

## Getting Started

### Setting Up the Environment
1. **Clone the Repository**:
   ```bash
   git clone git@github.com:GuiBo79/karly-book.git
   cd karly-book
   ```

2. **Build and Run the Application**:
   Use the Makefile commands to build the database, and run the application and services:

   - To build and run all services:
     ```bash
     make install
     ```
   - To run the application in another terminal:
     ```bash
     make app
     ```

### Accessing phpMyAdmin
- Once the services are up and running, phpMyAdmin can be accessed at `http://localhost:8080` (or the appropriate host and port based on your configuration).
- Log in using the MySQL credentials specified in your `docker-compose.yml` file.

### Using the Application
- The application will load data into the MySQL database and create views for analyzing fire incidents that can be exported using the UI to create reports.
- You can use phpMyAdmin to view and manage this data.

## Customization
- You can modify the Python script to adjust the data loading process.
- SQL queries for creating views used by reports can be modified in `sql_queries.py`.

## Troubleshooting
- Ensure Docker and Docker Compose are correctly installed and running.
- Check the Docker logs if any service fails to start.

- To run the MySql DB service manually:
     ```bash
     docker-compose up db
     ```
- To run the phpMyAdmin service manually:
     ```bash
     docker-compose up phpmyadmin
     ```
- To run the app service manually:
     ```bash
     docker-compose up app
     ```
IMPORTANT: do not kill the terminal, open a new one to run the services. 


