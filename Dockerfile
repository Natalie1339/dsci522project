FROM quay.io/jupyter/minimal-notebook:afe30f0c9ad8

COPY conda-lock.yml conda-lock.yml

RUN conda install -n base -c conda-forge conda-lock -y
RUN conda-lock install -n dockerlock conda-lock.yml
 