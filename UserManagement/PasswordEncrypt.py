#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

import hashlib

# 定义一个加密密钥, 默认为hello
register_secret = 'hello'


def sha1_encrypt(password: str, secret: str = register_secret) -> str:
    encrypt_string = secret + password
    sha1 = hashlib.sha1()
    sha1.update(encrypt_string.encode('utf-8'))
    return sha1.hexdigest()

