# Project Env
. $(dirname $0)/env.sh

# Determine Tag
IMAGE_TAG=tmp

# Docker Build
DOCKER_BUILDKIT=1 docker build . --build-arg LOGIQX_DEBUG -t $IMAGE_NAME:$IMAGE_TAG


# Copy the library scripts
docker run --rm --entrypoint cat $IMAGE_NAME:$IMAGE_TAG $WORK_DIR/python/constants.py >$PROJ_DIR/python/constants.py
docker run --rm --entrypoint cat $IMAGE_NAME:$IMAGE_TAG $WORK_DIR/python/common.py >$PROJ_DIR/python/common.py
docker run --rm --entrypoint cat $IMAGE_NAME:$IMAGE_TAG $WORK_DIR/python/name.py >$PROJ_DIR/python/name.py
docker run --rm --entrypoint cat $IMAGE_NAME:$IMAGE_TAG $WORK_DIR/python/fuzzy.py >$PROJ_DIR/python/fuzzy.py

# Clear pycache
rm -f $PROJ_DIR/python/__pycache__/*.*.pyc

# Remove the temporary tag to avoid <None> <None> at a later date
docker image rm $IMAGE_NAME:$IMAGE_TAG
