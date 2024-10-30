import hashlib

def calculate_sha256(file_path):
    # 创建SHA-256哈希对象
    sha256_hash = hashlib.sha256()

    # 读取文件并更新哈希对象
    with open(file_path, 'rb') as f:
        # 以块的方式读取文件，避免大文件占用过多内存
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    # 返回哈希值的十六进制表示
    return sha256_hash.hexdigest()

# 计算1.txt的SHA-256哈希值
file_path = '1.txt'
hash_value = calculate_sha256(file_path)
print(f'SHA-256 hash of {file_path}: {hash_value}')

