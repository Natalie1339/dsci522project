# Use Miniforge3 as a minimal Conda base image
FROM condaforge/miniforge3:latest

# Set the working directory
WORKDIR /workplace

# Copy conda-lock.yml into the container
COPY conda-lock.yml conda-lock.yml

# Install conda-lock in base environment
RUN conda install -n base -c conda-forge conda-lock -y

# Create a separate project environment from the lockfile
RUN conda-lock install -n dsci522project conda-lock.yml

# Register the environment as a Jupyter kernel
RUN /opt/conda/envs/dsci522project/bin/python -m ipykernel install \
    --user \
    --name dsci522project \
    --display-name "Python (dsci522project)"

# Expose JupyterLab port
EXPOSE 8888

# Start JupyterLab inside the dsci522project environment
CMD ["bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate dsci522project && jupyter lab --ip=0.0.0]()
