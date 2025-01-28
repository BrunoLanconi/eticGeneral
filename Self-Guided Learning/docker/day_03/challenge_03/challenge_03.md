# Challenge 03: Multi Container

Create a multi-container application using Docker Compose.

## Challenge

- Create a multi-container application using Docker Compose.
- The application must have at least two services.
- Each service must have its own Dockerfile.
- The images must be pushed to Docker Hub.
- The services must communicate with each other.
- The services must be connected to the same network.
- The services must be able to persist data using volumes.
- The services must be able to set the configuration using environment variables.
    
### Godlike Mode

- Create a Makefile to automate the process of building, running, and pushing the images.
- Use a `.env` file to set the environment variables.
- Add a health check to the services.
- Add a Makefile command to extract inspection data from the services to a file.
