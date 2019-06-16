# -*- coding:utf-8 -*-
import redis


class redisUtil:
    def __init__(self, host="172.16.0.211", db=13, password="", port="6379"):
        self.database = redis.Redis(host=host, port=port, db=db, password=password)
        print("successfully connect to redis server.")

    def set_data(self, key, value):
        self.database.set(key, value)

    def get_data(self, key):
        value = self.database.get(key)
        if value is None:
            return None
        else:
            return value.decode()

    def get_keys(self):
        byteKeys = self.database.keys()
        strKeys = []
        for key in byteKeys:
            strKeys.append(key.decode())
        return strKeys

    def delete_data(self, key):
        self.database.delete(key)

    def get_hash_keys(self, key):
        byteKeys = self.database.hkeys(key)
        strKeys = []
        for key in byteKeys:
            strKeys.append(key.decode())
        return strKeys


if __name__ == '__main__':
    redis_util = redisUtil()
    keys_list = redis_util.get_keys()
    print(keys_list)
    for hashkey in keys_list:
        print(hashkey)
        key = redis_util.get_hash_keys(hashkey)
        redis_util.delete_data(key)
        print("=======", key)
