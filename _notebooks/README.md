# Working on Notebooks

This section is written by me: Dockerfile at this level can be used to run JupyterLab

***

- `data` folder can contain any data files for notebooks, organized by nested folders per project
- `my_icons` stores any images used. When saved, will be converted along with notebook
- `_templates` has a template jupyter notebook for starting quickly. 

## Publishing

- Since you are using Jupytext to git track notebooks, you are not pushing `.ipynb` files to GitHub. This means the GitHub action will not make the notebook files into blog posts.
- Instead, use `make server` at the root directory to run the commands locally

## Vanillin 

### Run this project with vanillin 🍦

⚠️ **NOTICE**: Must run the following commands when in `_notebooks` from root directory

```
cd _notebooks
```

Build image:
```
vanillin website_work
```

Run JupyterLab:
```
vanillin website_work 10000
```

Don't have `vanillin` installed? Add as an `oh-my-zsh` plugin [here](https://github.com/zachbogart/vanillin#vanillin)

### Run this project manually

Build image:
```
docker build --rm -t website_work .
```

Run JupyterLab:
```
docker run --rm -p 10000:8888 -e JUPYTER_ENABLE_LAB=yes -v $PWD:/home/jovyan/work website_work
```

Don't have Docker installed? Download [here](https://docs.docker.com/get-docker/)


# Auto-convert Jupyter Notebooks To Posts

[`fastpages`](https://github.com/fastai/fastpages) will automatically convert [Jupyter](https://jupyter.org/) Notebooks saved into this directory as blog posts!

You must save your notebook with the naming convention `YYYY-MM-DD-*.ipynb`.  Examples of valid filenames are:

```shell
2020-01-28-My-First-Post.ipynb
2012-09-12-how-to-write-a-blog.ipynb
```

If you fail to name your file correctly, `fastpages` will automatically attempt to fix the problem by prepending the last modified date of your notebook. However, it is recommended that you name your files properly yourself for more transparency.

See [Writing Blog Posts With Jupyter](https://github.com/fastai/fastpages#writing-blog-posts-with-jupyter) for more details.