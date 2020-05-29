Commando's to run docker:
* `docker build -t fast .`
* `docker run -p 8080:8080 -it --name fast -e MODULE_NAME=fast.main -e LOG_LEVEL=debug -e PORT=8080 fast`