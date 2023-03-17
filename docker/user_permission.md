ISSUE:
```
➜ docker ps
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json: dial unix /var/run/docker.sock: connect: permission denied
```

The issue is due to you are not in docker group

To check if the current user is in dockger group you can check below file
```
cat /etc/group
```

To resolve the issue you can check the link https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue or follow below commands

SOLUTION:
```
1. Create the docker group if it does not exist
    sudo groupadd docker
2. Add your user to the docker group.
    sudo usermod -aG docker $USER
3. Run the following command or Logout and login again and run (that doesn't work you may need to reboot your machine first)
    newgrp docker
4. Check if docker can be run without root
    docker run hello-world
5. Reboot if still got error
    reboot
```
