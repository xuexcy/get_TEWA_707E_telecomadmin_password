# 获取电信 TEWA-707E 光猫超管密码
1. 准备 python3 虚拟环境: `sh create_venv.sh`
2. 使用 ftp 获取 db_user_cfg.xml 文件:
  - mac 上安装 lftp: `brew install lftp`
  - 执行 `sh get_xml.sh`
  - windows/linux 使用其他 ftp 软件，参考 `get_xml.sh` 获取文件
3. 从 db_user_cfg.xml 中获取超管账号名和密码: `sh get_password.sh`
4. 第三步里面会解码 db_user_cfg.decode.xml 并得到解码文件 db_user_cfg.decode.xml 文件，直接打开解码文件找到 `telecomadmin`, `Pass` 字段就是超管密码

# 参考
1. 文章里用的 python2 代码, mac 电脑默认已经没有 python2 了: https://blog.liqiye.com/posts/3839389167/index.html

# 其他
1. 公网访问: 超管账号登录后，安全 -> 防火墙 -> 攻击保护设置 -> 防攻击保护【关闭】
