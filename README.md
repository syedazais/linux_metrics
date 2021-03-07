# linux_metrics
# step1: make sure docker is running by executing below command.
# docker service docker start
# step 2: build an image and create name as metrics under current directory where dockerfile placed.
# docker build -t metrics .
# make sure image has created as name metrics. To validate execute below command.
# docker images
# step3: run docker container and execute python script inside container.
# docker run -it metrics metrics.py
