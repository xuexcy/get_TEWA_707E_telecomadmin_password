from Crypto.Cipher import AES
from binascii import a2b_hex

KEY = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

def decrypt(text_hex):
    """解密十六进制字符串，自动处理非16倍数的数据"""
    # 将十六进制转为字节
    data = a2b_hex(text_hex)
    
    # 计算需要补齐的字节数
    padding_len = (16 - len(data) % 16) % 16
    
    # 补齐数据（用0填充，你也可以用PKCS#7，但天邑用0填充）
    if padding_len > 0:
        data = data + b'\x00' * padding_len
    
    # AES ECB 解密
    cryptor = AES.new(KEY, AES.MODE_ECB)
    plain_data = cryptor.decrypt(data)
    
    # 去掉填充的字节
    if padding_len > 0:
        plain_data = plain_data[:-padding_len]
    
    return plain_data


cfg_file = open("db_user_cfg.xml", "rb")
dec_file = open("db_user_cfg.decode.xml", "w")

# 读取文件头（前60字节，包含文件格式信息）
file_header = cfg_file.read(60)
print("文件头:", file_header[:20].hex())

trunk_index = 0
while True:
    # 读取12字节的块信息（实际大小、存储大小、下一个块位置）
    trunk_info = cfg_file.read(12)
    if len(trunk_info) < 12:
        print("读取块信息失败，文件可能已结束")
        break
    
    trunk_real_size = int.from_bytes(trunk_info[0:4], byteorder='big')
    trunk_size = int.from_bytes(trunk_info[4:8], byteorder='big')
    next_trunk = int.from_bytes(trunk_info[8:12], byteorder='big')
    
    print(f"块 {trunk_index}: 实际大小={trunk_real_size}, 存储大小={trunk_size}, 下一个块={next_trunk}")
    
    # 根据存储大小读取加密数据
    trunk_data = cfg_file.read(trunk_size)
    if len(trunk_data) < trunk_size:
        print(f"警告：块 {trunk_index} 实际读取 {len(trunk_data)} 字节，预期 {trunk_size} 字节")
        break
    
    # 解密并写入（只写入实际大小的数据，而不是补齐后的整个块）
    decrypted = decrypt(trunk_data.hex())
    
    # 只取实际有用的数据（前 trunk_real_size 字节）
    decrypted = decrypted[:trunk_real_size]
    
    # 解码为UTF-8并写入
    try:
        dec_file.write(decrypted.decode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"块 {trunk_index} 写入失败: {e}")
        # 直接写入字节数据（如果解码失败）
        dec_file.write(decrypted.decode('latin-1', errors='replace'))
    
    trunk_index += 1
    
    # 检查是否还有下一个块
    if next_trunk == 0:
        print("所有块处理完毕")
        break

cfg_file.close()
dec_file.close()
print(f"\n解密完成！输出文件: db_user_cfg.decode.xml")
