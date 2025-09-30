# Basic_Docker

A lightweight reference for common Docker commands, now available as both a README and a small web experience.

## Install Docker

credit: https://docs.docker.com/engine/install/ubuntu/

## Install Portainer with Docker on Linux

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

### ตรวจสอบ volume
```
docker volume ls
```

### ลบ volume
```
docker volume rm <volume name>
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

## Running the web server

Serve the same list of Docker commands in a browser by starting the bundled Python web server:

```bash
python server.py --host 0.0.0.0 --port 8000
```

Once running, open `http://localhost:8000` in your browser to view the command reference. Press `Ctrl+C` in the terminal to stop the server.
