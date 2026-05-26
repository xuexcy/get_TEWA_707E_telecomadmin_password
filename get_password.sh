#!/bin/bash
########################################################################
#
# Copyright (c) 2026 xx.com, Inc. All Rights Reserved
#
########################################################################
# Author : xuechengyun
# E-mail : xuechengyunxue@gmail.com
# Date   : 2026/05/16 22:17:38
# Desc   :
########################################################################

# set -x
CUR_DIR=$(cd `dirname $0`; pwd)
cd ${CUR_DIR}

SCRIPT_DIR=${CUR_DIR}

if [ "${BASH_SOURCE[0]}" != "" ];
then
    SCRIPT_DIR=$(cd `dirname ${BASH_SOURCE[0]}`; pwd)
fi

source ./python3_venv/bin/activate
# 解码 db_user_cfg.xml
python decode.py > /dev/null
# 找到账号名和密码
awk -F'val="' '/telecomadmin/{print $2}' db_user_cfg.decode.xml | awk -F'"' '{print $1}'








