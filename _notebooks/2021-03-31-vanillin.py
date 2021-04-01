# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # "Vanillin: A Smooth Jupyter/Docker Setup"
# > "Making a template and alias to remove the rough edges of working on Jupyter Notebooks within Docker containers"
#
# - toc: false
# - branch: master
# - badges: false
# - comments: true
# - categories: [docker, jupyter]
# - image: "images/thumbnails/19385755595_0080a20e99_c.jpeg"
# - hide: false
# - search_exclude: false

# ![](my_icons/noun_happy_ice_cream_3644324.png)

# I find that I mostly work on getting things to work so I can then do work.
#
# Does that last sentence work?

# Basically, most of the time I'm not doing analyses or visualizing something cool. Instead I'm setting up an environment or making sure things are pointing at the right files or whatever. I'm getting things ready a lot, so I wanted to try smooth out some of the hassle of setting things up.

# So, I made [a little template called vanillin](https://github.com/zachbogart/vanillin) to setup a project quickly, allowing me to work out of Docker and code in Jupyter Notebooks with a few of the sharp edges removed.

# ![](my_icons/vanillin_docker_build.png)
# ![](my_icons/vanillin_docker_run.png)

# ## 👁️💖👨‍💻📙's (I love code notebooks)

# To backup, let's start with "I like coding in notebooks".
#
# [Jupyter notebooks](https://jupyter.org/) are great. You can see what is happening for every cell. I do most of my work in Jupyter Notebooks with Python. [Observable](https://observablehq.com) is also super cool, although I'm less familiar with JavaScript, but learning about it will definitely be through that medium. 
#
# I like the code notebook. But they require a bit of setup each time. And keeping track of all that can be a pain. Mostly it's keeping track of Python.

# ## Why'd it have to be snakes

# I've always been told that working in Python, you have to work out of [virtual environments](https://docs.python.org/3/tutorial/venv.html). The annoying thing I've found about this is sharing notebooks with other people. Collaborators have their own setup and make their own environments. It is annoying to keep track of. People have made a lot of tools like [pipenv](https://realpython.com/pipenv-guide/) and [Poetry](https://python-poetry.org/), or general practices like [requirements.txt](https://www.idkrtm.com/what-is-the-python-requirements-txt/), but I find it a bit of a hassle because I only want to run a jupyter notebook. After all of the generating and setup, we are working out of a browser in jupyter. It would be nice if when sharing notebooks I wouldn't have to worry so much about the environment they are run in. I just want a command that builds up an environment and gets me inside the jupyter environment.
#
# In other words, I want to limit the amount of time I worry about my kitchen and instead focus on cooking.
#
# Turns out to do this, you kind of have to think a lot about kitchens first.

# ## Trying to Make it Myself

# My first attempt was to make my own kitchen from scratch. I was using Docker to make custom environments for each project. This worked, but it was a hassle, since it was a lot of things to manage.
# - Had to [make custom environments for different use cases and host them on DockerHub](https://github.com/zachbogart/pyro)
# - Had to maintain all that stuff
#
# Rather than making things easier to use, it was just a hassle to handle. I wasn't very familiar with Docker and I wanted to leave the maintenance to people with more experience. 
#
# Turns out Jupyter already had this setup...setup.

# ## Using Jupyter Docker Stacks
#
# Came across the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) and that made things a lot simpler. They maintain docker images and I can pull the ones I want to run jupyter notebooks. When I'm working out of the images, I can be a lot less worried about installing things. I also can now pass a notebook along with a Dockerfile and know it'll run for someone. Then we can actually collaborate rather than keep asking questions about how our machines are working.
#
# This setup still is a bit of a hassle. These docker commands are quite intimidating:
# ```
# docker build --rm -t DOCKER_IMAGE_NAME .
# docker run --rm -p 10000:8888 -e JUPYTER_ENABLE_LAB=yes -v $PWD:/home/jovyan/work DOCKER_IMAGE_NAME
# ```
#
# When I run these, I only ever change the image name and the port. So let's smooth that out a bit.

# ## Smooth and Creamy

# Vanillin is not that fancy. It's just [a blank repo](https://github.com/zachbogart/vanillin) and [an ohmyzsh plugin](https://gist.github.com/zachbogart/c01e88886855c39c4058d0baa43ec9ec), but makes it much easier to just get cooking quickly.
#
# - Dockerfile is taking a base image from the Jupyter Docker Stacks. And I can pick the fanciest kitchen they have for no extra cost. They have [a bunch to pick from](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html) if size is a big issue.
# - Additional packages I may need can be installed in the Dockerfile or run in a notebook cell
# - Command to start things up is similar to `jupyter notebook`, trying to be as easy to use as possible
#
# ```
# vanillin DOCKER_IMAGE_NAME # build command
# vanillin DOCKER_IMAGE_NAME 10000 # run notebook on port 10000
# ```
#
# It's not actually doing much, but I find it much more user-friendly.
#
# **A lot of ice cream**: The drawback of this setup is the images are big. The fancy kitchen does come at a cost of the size of 1-2 GB. But it handles everything. I think it's a good tradeoff.
#
# ![](my_icons/vanillin_help.png)

# ## Mmm...Vanillin

# I'm sure I'll soon find a smoother way to code things up in code notebooks, but right now this setup has been very helpful.
# - Have smart people handle docker containers/images
# - Make a Dockerfile that suits the needs of a project
# - Get going! Start up jupyter easily. Install things without getting goosebumps. Share work with others without a bunch of back and forth ([jupytext](https://github.com/mwouts/jupytext) does help as well).
#
# Make a mess in the kitchen. Cook up something tasty.
#
# That's it. Feel free to [give vanillin a try](https://github.com/zachbogart/vanillin). Hope you are doing well.
#
# Till next time!

# ![](https://media.giphy.com/media/xT5LML9tsaLhr7ThUk/giphy.gif)

# #### Image Credit
# - [happy ice cream](https://thenounproject.com/search/?creator=4129988&q=happy&i=3644324) by Zach Bogart from the [Noun Project](https://thenounproject.com/zachbogart/)
# - [Making ice cream bars](https://www.flickr.com/photos/alberta_archives/19385755595/in/photolist-vx44Kr-5niFbH) from "Provincial Archives of Alberta" on Flickr Commons


