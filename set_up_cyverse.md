Setup

```
git init
git remote add origin https://github.com/kulpojke/pdal-pipelines.git
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=43200'
git config --global user.email michaelhuggins@protonmail.com
git config --global user.name michael
git pull origin
git checkout main

conda env create
source activate pycrown-env
python setup.y install
conda deactivate
python -m ipykernel install --user --name=pycrown-env
```

Now you will be able to use this kernel in the notebook