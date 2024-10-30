from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# 生成一个随机的密钥和IV
key = os.urandom(32)  # AES-256
iv = os.urandom(16)   # AES块大小为16字节

def encrypt_file(input_file, output_file):
    # 创建AES加密器
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # 使用PKCS7填充
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    padded_data = padder.update(plaintext) + padder.finalize()
    
    # 加密
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # 将密文和IV写入输出文件
    with open(output_file, 'wb') as f:
        f.write(iv)  # 前16字节为IV
        f.write(ciphertext)

def decrypt_file(input_file, output_file):
    # 读取密文和IV
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # 前16字节为IV
        ciphertext = f.read()
    
    # 创建AES解密器
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # 解密
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    # 使用PKCS7去填充
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    
    # 将解密后的数据写入输出文件
    with open(output_file, 'wb') as f:
        f.write(plaintext)

# 使用示例
encrypt_file('1.txt', 'encrypted_file.bin')
decrypt_file('encrypted_file.bin', 'decrypted_file.txt')

