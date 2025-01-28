# Common Techniques for Troubleshooting

## [Check Container Logs](https://docs.docker.com/reference/cli/docker/container/logs/)

Use the command alias `docker logs` command to view the logs of a container. This can help you identify any errors or issues that the container is experiencing. This command is an alias for `docker container logs`.

### Example
```bash
docker logs <container_id>
```

The `container_id` can be obtained using the `docker ps` command.

## Inspect Container

Use the command alias `docker inspect` to view detailed information about a container. This can help you identify the container's configuration, status, and other useful information. This command is an alias for `docker container inspect`.

### Example
```bash
docker inspect <container_id>
```

You should see something like this:

### Example
```json
[
    {
        ...
        "State": {
            "Status": "running",
            "Running": true,
            ...
            "ExitCode": 0,
            "Error": "",
            ...
        },
        "HostConfig": {
            ...
            "NetworkMode": "app-network",
            "PortBindings": {
                "5432/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "5432"
                    }
                ]
            },
            ...
        },
        "NetworkSettings": {            
            "Networks": {
                "app-network": {
                    ...
                    "DNSNames": [
                        "postgres",
                        "d500698b0c1a"
                    ]
                }
            }
        },
        "Mounts": [
            {
                "Type": "volume",
                ...
                "Source": "/var/lib/docker/volumes/0b197564a36c32650e578bd73a8e1536be18d28fb35dfbdff7aa9d90a60b3b44/_data",
                "Destination": "/var/lib/postgresql/data",
                ...
            }
        ],
        "Config": {
            ...
            "Env": [
                "POSTGRES_USER=postgres",
                "POSTGRES_PASSWORD=postgres",
                "POSTGRES_DB=postgres",
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/14/bin",
                "GOSU_VERSION=1.17",
                "LANG=en_US.utf8",
                "PG_MAJOR=14",
                "PG_VERSION=14.13-1.pgdg120+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "postgres",
            "Volumes": {
                "/var/lib/postgresql/data": {}
            },
            "WorkingDir": "",
            "Entrypoint": [
                "docker-entrypoint.sh"
            ],
            ...
        }        
    }
]
```

This information is nice to check the container status and configuration, for example:

- `State.Status`: The status of the container (e.g., running, stopped)
- `State.Running`: Whether the container is running
- `State.ExitCode`: The exit code of the container
- `State.Error`: Any error message
- `HostConfig.NetworkMode`: The network mode of the container
- `HostConfig.PortBindings`: The port bindings of the container
- `Config.Env`: The environment variables of the container
- `Config.Cmd`: The command that was run when the container was started
- `Config.Image`: The image used to create the container
- `Config.Volumes`: The volumes used by the container
- `Mounts`: The mounts used by the container, precisely `Type`, `Source`, and `Destination`
- `NetworkSettings.Networks.*.DNSNames`: The networks the container is connected to