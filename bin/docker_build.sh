# Project Env
. $(dirname $0)/env.sh

# Determine the temporary (build) tag from the git commit ID
FINAL_TAG=$IMAGE_TAG
IMAGE_TAG=$(git rev-parse --short=12 HEAD)

# Docker Build
DOCKER_BUILDKIT=1 docker build . --build-arg LOGIQX_DEBUG -t $IMAGE_NAME:$IMAGE_TAG

# Run daily reporting
run_py_script results.py

# Run series reporting
#run_py_script series.py

# Apply release tag, removing earlier tag / image if required
if [ -n "$(docker image ls -q $IMAGE_NAME:$FINAL_TAG)" ]
then
    docker image rm $IMAGE_NAME:$FINAL_TAG >/dev/null
fi
docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:$FINAL_TAG

# Apply "latest" tag, removing earlier tag / image if required
if [ -n "$(docker image ls -q $IMAGE_NAME:latest)" ]
then
    docker image rm $IMAGE_NAME:latest >/dev/null
fi
docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:latest

# Remove the temporary tag to avoid <None> <None> at a later date
docker image rm $IMAGE_NAME:$IMAGE_TAG >/dev/null
