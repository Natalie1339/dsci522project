# Use Miniforge3 as a minimal Conda base image
FROM condaforge/miniforge3:latest

# install for make command
RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workplace

# Copy conda-lock.yml into the container
COPY conda-lock.yml conda-lock.yml

# Install conda-lock tool in base environment
RUN conda install -n base -c conda-forge conda-lock -y

# Create a reproducible environment from the lockfile
RUN conda-lock install -n dsci522project conda-lock.yml

# Register dsci522project environment as a Jupyter kernel
RUN /opt/conda/envs/dsci522project/bin/python -m ipykernel install --user --name dsci522project --display-name "Python (dsci522project)"

# Expose JupyterLab port
EXPOSE 8888

# Make dsci522project the default environment
RUN echo "conda activate dsci522project" >> ~/.bashrc

# Set environment variables so the environment is active by default
ENV PATH /opt/conda/envs/dsci522project/bin:$PATH

# Start JupyterLab from the dsci522project environment
CMD ["bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate dsci522project && jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root"]

