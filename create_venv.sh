#!/bin/bash
########################################################################
#
# Copyright (c) 2026 xx.com, Inc. All Rights Reserved
#
########################################################################
# Author  :   xuechengyun
# E-mail  :   xuechengyunxue@gmail.com
# Date    :   2026/05/17 14:07:57
# Desc    :
########################################################################

# set -x
CUR_DIR=$(cd `dirname $0`; pwd)
cd ${CUR_DIR}

python3 -m venv python3_venv
# 激活 venv
source ./python3_venv/bin/activate
#安装 cryptodome
pip3 install pycryptodome


cd -
