# Basic_Docker
# Install Docker
credit: https://docs.docker.com/engine/install/ubuntu/
# Install Portainer with Docker on Linux
credit: https://docs.portainer.io/v/ce-2.11/start/install/server/docker/linux
## Docker-Commands
### ตรวจสอบเวอชั่นของ Docker
```
docker version
```
### ตรวจสอบ images ในเครื่องของเรา
```
docker images
```
### ลบ images ในเครื่องของเรา
```
docker image rm [OPTIONS] IMAGE [IMAGE...]
```
### ตรวจสอบรายละเอียดเพิ่มเติม
```
docker inspect <container name>
```
### แสดงรายการ container
```
docker ps -a
```
### สั่งเริ่มการทำงานcontainer จาก container id
```
docker start <container id>
```
### หยุดการทำงาน container จาก container id
```
docker stop <container id>
```
### ลบ container จาก container id
```
docker rm <container id>
```
