#!/bin/bash
########################################################################
#
# Copyright (c) 2026 xx.com, Inc. All Rights Reserved
#
########################################################################
# Author : xuechengyun
# E-mail : xuechengyun@gmail.com
# Date   : 2026/05/16 21:59:05
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

HOST="192.168.1.1"
USER="useradmin"

echo "请输入光猫密码: "
read -s PASS
echo

# mac 电脑使用 lftp, windows 或 linux 使用 ftp 软件
lftp -u ${USER},${PASS} ${HOST} << EOF
cd /userconfig/cfg
get db_user_cfg.xml
quit
EOF
