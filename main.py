import docker

def deploy_apache(image_name, container_name, port_mapping):
    # Create a Docker client
    client = docker.from_env()

    try:
        # Check if the container with the specified name already exists
        existing_container = client.containers.get(container_name)
        print(f"Container '{container_name}' already exists. Stopping and removing...")
        existing_container.stop()
        existing_container.remove()
    except docker.errors.NotFound:
        pass

    # Pull the specified Docker image
    print(f"Pulling Docker image: {image_name}")
    client.images.pull(image_name)

    # Run the Apache container
    print(f"Running Apache container: {container_name}")
    client.containers.run(
        image=image_name,
        name=container_name,
        detach=True,
        ports={f"{port_mapping}/tcp": port_mapping},
    )

    print(f"Apache container '{container_name}' is now running on port {port_mapping}")

if __name__ == "__main__":
    # Specify Docker image name, container name, and port mapping
    apache_image = "httpd:latest"  # You can change this to a specific Apache version
    apache_container = "apache_container"
    apache_port_mapping = 8080

    # Deploy Apache container
    deploy_apache(apache_image, apache_container, apache_port_mapping)
