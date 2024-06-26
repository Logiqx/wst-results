PROJ_DIR=$(realpath $(dirname $0)/..)
PROJ_NAME=$(basename $PROJ_DIR)

IMAGE_NAME=logiqx/$PROJ_NAME
IMAGE_TAG=1.0.0

WORK_DIR=/home/jovyan/work/sse-results

run_py_script()
{
  docker run -it --rm \
         --dns 192.168.0.254 \
         --mount type=bind,src=$PROJ_DIR/events,dst=$WORK_DIR/events \
         --mount type=bind,src=$PROJ_DIR/config,dst=$WORK_DIR/config \
         --mount type=bind,src=$PROJ_DIR/docs,dst=$WORK_DIR/docs \
         $IMAGE_NAME:${IMAGE_TAG:-latest} python/$1
}

# Explanation at https://www.peterbe.com/plog/set-ex
set -ex

cd $PROJ_DIR
