# Dockerfile
# 2021-02-22
#

# Start from a core stack version
# https://hub.docker.com/r/jupyter/datascience-notebook/tags?page=1&ordering=last_updated&name=lab-3.0.5
# ref: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-datascience-notebook
FROM jupyter/datascience-notebook:lab-3.0.5

# Jupytext (easier to version control)
# ref: https://jupytext.readthedocs.io/en/latest/
RUN pip install jupytext==1.10.2

# Spellchecker while writing markdown
# https://github.com/jupyterlab-contrib/spellchecker
RUN pip install jupyterlab-spellchecker