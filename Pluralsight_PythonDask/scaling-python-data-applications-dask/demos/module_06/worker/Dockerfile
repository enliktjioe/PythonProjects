FROM continuumio/anaconda3

WORKDIR /tmp
ENTRYPOINT ["dask-worker", "scheduler:8786", "--nthreads", "1"]
