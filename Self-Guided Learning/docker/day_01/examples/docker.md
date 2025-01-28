## [Virtual Machines and Containers](https://aws.amazon.com/compare/the-difference-between-docker-vm/)

The difference between virtual machines and containers is that virtual machines are an abstraction of physical hardware turning one server into many servers, while containers are an abstraction at the app layer that packages code and dependencies together. Containers are lightweight and use the host OS to run, whereas virtual machines require a guest OS.

---

## [Docker](https://www.docker.com/) and Containerization

Docker is a platform for developing, shipping, and running applications using containerization. Containerization is a lightweight alternative to full machine virtualization that involves encapsulating an application in a container with its own operating environment.

### How does it work?

Docker runs applications in containers, which are isolated environments containing everything needed to run an application, including libraries, dependencies, and configuration files. Containers are created from images, which are read-only templates that define the application's environment. Images are stored in a registry, such as Docker Hub, and can be shared and reused.

### Key Concepts

- **Containers**: Runnable instances of images.
- **Docker Compose**: A tool for defining and running multi-container Docker applications.
- **Docker Engine**: A client-server application that builds and runs containers.
- **Docker Hub**: A cloud-based registry service for sharing and storing container images.
- **Docker Registry**: A storage and distribution system for named Docker images.
- **Dockerfile**: A text file that defines how to build an image.
- **Images**: Read-only templates used to create containers.

### Why this is necessary?

Containerization offers several benefits, including:

- **Efficiency**: Containers share the host OS kernel, reducing overhead and improving performance.
- **Isolation**: Containers are isolated from each other, preventing conflicts and security vulnerabilities.
- **Portability**: Containers can run on any system that supports the containerization platform.
- **Scalability**: Containers can be easily scaled up or down to meet demand.
