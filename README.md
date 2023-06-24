# python3-nbctl

将ipynb文件转化为hugo markdown文件/Convert ipynb to hugo markdown files

[![PyPI-python3-nbctl](https://img.shields.io/pypi/v/python3-nbctl.svg?maxAge=3600)](https://pypi.org/project/python3-nbctl/)

Github Actions for [Container ipynb to markdown](https://github.com/marketplace/actions/nbctl)

## How to Use by Github Actions

```
      - name: install nbctl
        uses: x-actions/python3-nbctl@v1
      - name: convert ipynb to hugo markdown
        run: |
          find static/code/ai -type f -name "*.ipynb" | grep -v ".ipynb_checkpoints" | xargs -I{} nbctl --input {} -f
```

## Dev and Test

- local run

```
# install
pip3 install -r requirements.txt
python3 setup.py install

# or
pip3 install python3-nbctl

# run
nbctl
```
