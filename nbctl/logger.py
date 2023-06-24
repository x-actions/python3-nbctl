#  Copyright 2020 xiexianbin.cn
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

"""python logger utils."""

import logging
import sys

from nbctl import constants


def gen_logger(level=constants.LOG_LEVEL):
    # create logger
    if level == 'DEBUG':
        log_level = logging.DEBUG
    elif level == 'INFO':
        log_level = logging.INFO
    elif level == 'WARN':
        log_level = logging.WARN
    elif level == 'ERROR':
        log_level = logging.ERROR
    elif level == 'FATAL':
        log_level = logging.FATAL
    else:
        log_level = logging.DEBUG
    formatter = logging.Formatter(
        fmt="%(asctime)-15s %(process)d - %(filename)s:%(lineno)d %(levelname)s %(message)s",
        datefmt="%a %d %b %Y %H:%M:%S")

    _logger = logging.getLogger(name="nbctl")
    _logger.setLevel(log_level)

    # fh = logging.FileHandler(filename="nbctl.log")
    # fh.setLevel(log_level)
    # fh.setFormatter(formatter)
    # _logger.addHandler(fh)

    oh = logging.StreamHandler(sys.stdout)
    oh.setLevel(log_level)
    oh.setFormatter(formatter)
    _logger.addHandler(oh)
    return _logger


logger = gen_logger(constants.DEFAULT_LOG_LEVEL)
