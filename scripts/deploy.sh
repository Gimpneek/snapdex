# build the docker image and push to an image repository
docker tag $IMAGE_REPO_URL:$TRAVIS_TAG $IMAGE_REPO_URL:$TRAVIS_TAG
docker push $IMAGE_REPO_URL:$TRAVIS_TAG

# update an AWS ECS service with the new image
bash scripts/ecs-deploy.sh -c $CLUSTER_NAME -n $SERVICE_NAME -i $IMAGE_REPO_URL:$TRAVIS_TAG