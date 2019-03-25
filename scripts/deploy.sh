# install AWS SDK
pip install awscli
export PATH=$PATH:$HOME/.local/bin

# install necessary dependency for ecs-deploy
sudo add-apt-repository ppa:eugenesan/ppa -y
sudo apt-get update -y
sudo apt-get install jq -y

# or login DockerHub
echo $DOCKER_HUB_PASSWORD | docker login --username $DOCKER_HUB_USER --password-stdin

# build the docker image and push to an image repository
docker build -t $IMAGE_REPO_URL .
docker tag $IMAGE_REPO_URL:$TRAVIS_TAG $IMAGE_REPO_URL:$TRAVIS_TAG
docker push $IMAGE_REPO_URL:$TRAVIS_TAG

# update an AWS ECS service with the new image
bash scripts/ecs-deploy.sh -c $CLUSTER_NAME -n $SERVICE_NAME -i $IMAGE_REPO_URL:$TRAVIS_TAG