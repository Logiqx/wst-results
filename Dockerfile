# Base image versions
ARG NOTEBOOK_VERSION=notebook-6.4.6
ARG SSE_RESULTS_VERSION=1.1.2

# Jupyter notebook image is used as the builder
FROM jupyter/base-notebook:${NOTEBOOK_VERSION} AS builder

# Copy the required project files
WORKDIR /home/jovyan/work/sse-results
COPY --chown=jovyan:users python/*.ipynb ./python/
COPY --chown=jovyan:users python/templates/*.html ./python/templates/

# Convert Jupyter notebooks to regular Python scripts
RUN jupyter nbconvert --to python python/*.ipynb && \
    rm python/*.ipynb

# Ensure project file permissions are correct
RUN chmod 755 python/*.py

# Create final image from Speed Sailing Event Results
FROM logiqx/sse-results:${SSE_RESULTS_VERSION}

# Copy project files from the builder
COPY --from=builder --chown=jovyan:jovyan /home/jovyan/work/sse-results/ ./
