# Select Dockerfile base image
FROM nginx:alpine

# Copy index.html file to default nginx HTML lookup
COPY index.html /usr/share/nginx/html/index.html

# Copy entrypoint.sh to working directory
COPY entrypoint.sh ./entrypoint.sh

RUN chmod a+x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
