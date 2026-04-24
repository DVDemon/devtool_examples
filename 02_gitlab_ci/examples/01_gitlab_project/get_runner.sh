docker run -d --name gitlab-runner \
  -v ./config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --privileged \
  gitlab/gitlab-runner:latest run

