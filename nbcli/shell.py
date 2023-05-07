#  Copyright 2023 xiexianbin.cn
#  All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#         http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""convert ipynb to hugo markdown."""

import nbformat
from traitlets.config import Config
from nbconvert import MarkdownExporter

from nbctl import logger


class Nbcli(object):

    def __init__(self):
        pass

    def do(self, p: str):
        content = ""
        with open(p, 'r') as f:
            content = ''.join(f.readlines())

        jake_notebook = nbformat.reads(content, as_version=4)

        for i in jake_notebook.cells:
            logger.Debug(f'cell_type: {i.cell_type}, i: {i}')

        md_exporter = MarkdownExporter()
        (body, resources) = md_exporter.from_notebook_node(jake_notebook)

        print(f'body:\n{body}')
        print(f'resources:\n{resources}')

def main():
    cli = Nbcli()
    cli.do()


if __name__ == "__main__":

    main()
