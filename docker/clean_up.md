### Stop all running containers
docker stop $(sudo docker ps -aq)
### Remove all stopped containers
docker rm $(sudo docker ps -aq)
### Remove all images
docker rmi $(sudo docker images -a -q)
### Remove all volumes
docker volume prune
### Remove all dangling volumes
docker volume rm $(sudo docker volume ls -qf dangling=true)
### Remove all dangling networks
docker network rm $(sudo docker network ls -qf dangling=true)
### Remove all networks, volumes, images, containers, etc.
docker system prune -a
