# python3-nbctl

将ipynb文件转化为markdown文件/convert jupyter *.ipynb file to markdown files

[![PyPI-python3-nbctl](https://img.shields.io/pypi/v/python3-nbctl.svg?maxAge=3600)](https://pypi.org/project/python3-nbctl/)

Github Actions for [Container ipynb to markdown](https://github.com/marketplace/actions/nbctl)

## How to Use by Github Actions

```
      - name: convert jupyter *.ipynb file to markdown
        uses: x-actions/python3-nbctl@v1
        with:
          script: >
            find <path> -type f -name "*.ipynb" | grep -v ".ipynb_checkpoints" | xargs -I{} nbctl --input {} --force --debug
```

## Dev and Test

- local run

```
# install
pip3 install -r requirements.txt
python3 setup.py install

# or
pip3 install python3-nbctl
```

- help

```
nbctl --help
```
