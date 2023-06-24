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

"""convert jupyter *.ipynb file to markdown"""

import argparse
import os
import sys
from typing import Dict

import nbformat
from nbconvert import MarkdownExporter
from traitlets.config import Config

from nbctl import constants
from nbctl import logger


parser = argparse.ArgumentParser(description='convert jupyter *.ipynb file to markdown')
parser.add_argument('--debug', '-d', help='show debug info, default is INFO',
                    action="store_true")
parser.add_argument('--input', '-i', help='input *.ipynb file or dir', 
                    required=True, default='', type=str)
parser.add_argument('--output', '-o', help='output file or dir', 
                    required=False, default='', type=str)
parser.add_argument('--force', '-f', help='force overwrite output file', 
                    action="store_true")
args = parser.parse_args()


class nbctl(object):

    def __init__(self, input: str, output: str, debug: bool=False, force: bool=False):
        self.input = input
        self.output = output
        self.logger = logger.logger
        self.debug = debug
        if self.debug:
            self.logger = logger.gen_logger(constants.LOG_LEVEL)
            self.logger.debug(f'run in debug model...')
        self.force = force

        # Setup config
        self.config = Config()

    def _parse_metadata(self, info: str) -> Dict:
        if '\n' in info:
            info = info.split('\n')
        metadate = dict()
        for i in info:
            if i == '---':
                continue
            if ': ' in i:
                key, value = i.split(': ')
                metadate[key] = value
        return metadate

    def render_one(self, ipynb_path: str, markdown_dir: str) -> bool:
        # ipynb convert
        content = ''
        with open(ipynb_path, 'r') as f:
            content = ''.join(f.readlines())
        jake_notebook = nbformat.reads(content, as_version=4)

        for i in jake_notebook.cells:
            self.logger.debug(f'cell_type: {i.cell_type}, i: {i}')

        md_exporter = MarkdownExporter()  # config=self.config
        (body, resources) = md_exporter.from_notebook_node(jake_notebook)

        self.logger.debug(f'body:\n{body}')
        self.logger.debug(f'resources:\n{resources}')

        # output dir
        if not markdown_dir:
            self.logger.debug(f'[{ipynb_path}] not -o/--output set, try to parse output from .ipynb file ...')
            metadata = self._parse_metadata(jake_notebook.cells[0]['source'])
            _output = metadata.get('output', None)
            if _output:
                markdown_dir = _output
            if not markdown_dir:
                self.logger.warning(f'parse output from [{ipynb_path}] file failed.')
                return False
        if not os.path.exists(markdown_dir):
            os.system(f'mkdir -p {markdown_dir}')

        # output path
        markdown_name = f"{'.'.join(os.path.basename(ipynb_path).split('.')[:-1])}.md"
        markdown_path = os.path.join(markdown_dir, markdown_name)
        if os.path.isfile(markdown_path):
            self.logger.warning(f'file {markdown_path} is already exists, use -f/--force overwrite.')
            if not self.force:
                return False

        # write to file
        with open(markdown_path, "w") as f:
            f.writelines(body)

        return True


    def do(self):
        # check param
        if os.path.exists(self.input):
            if os.path.isdir(self.input):
                for (dirpath, dirnames, filenames) in os.walk(self.input):
                    self.logger.debug(f'dirpath: {dirpath}, dirnames: {dirnames}, filenames: {filenames}')
            else:
                self.render_one(ipynb_path=self.input, markdown_dir=self.output)
        else:
            print(f'dir {self.input} not exists, exit 1.')
            sys.exit(1)

        return True


def main():
    input = args.input
    if not input:
        print(f'not -i/--input set')
        parser.print_help()
        sys.exit(1)

    try:
        client = nbctl(input, args.output, debug=args.debug, force=args.force)
        client.do()
    except Exception as e:
        print(e)
        raise

if __name__ == "__main__":
    main()
