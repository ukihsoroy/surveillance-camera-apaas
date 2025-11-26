import configparser

def get_apaas_env():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    # 本地文件夹目录地址
    path = config['app']['path']

    # apaas的client id、secret
    client_id = config['apaas']['client_id']
    client_secret = config['apaas']['client_secret']
    namespace = config['apaas']['namespace']

    return path, client_id, client_secret, namespace
