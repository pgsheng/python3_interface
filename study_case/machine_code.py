"""
 @Author  : pgsheng
 @Time    : 2019/6/25 16:33
"""
# 功能说明：用户运行程序后，自动检测认证状态，如果未经认证，就需要注册。注册过程是用户将程序运行后显示的机器码（卷序号）发回给管理员，管理员通过加密后生成加密文件或字符串给回用户。
# 每次登录，在有注册文件或者注册码的情况下，软件就会通过DES和base64解码，如果解码后和重新获取的机器码一致，则通过认证，进入主程序。

import base64
import win32api

from pyDes import *


# from binascii import a2b_hex    #如果需要用二进制编码保存注册码和注册文件可以使用binascii转换

class register:
    def __init__(self):
        self.Des_Key = "BHC#@*UM"  # Key
        self.Des_IV = "\x22\x33\x35\x81\xBC\x38\x5A\xE7"  # 自定IV向量

    # 获取C盘卷序列号
    # 使用C盘卷序列号的优点是长度短，方便操作，比如1513085707，但是对C盘进行格式化或重装电脑等操作会影响C盘卷序列号。
    # win32api.GetVolumeInformation(Volume Name, Volume Serial Number, Maximum Component Length of a file name, Sys Flags, File System Name)
    # return('', 1513085707, 255, 65470719, 'NTFS'),volume serial number is  1513085707.
    def getCVolumeSerialNumber(self):
        CVolumeSerialNumber = win32api.GetVolumeInformation("C:\\")[1]
        # print chardet.detect(str(CVolumeSerialNumber))
        # print CVolumeSerialNumber
        if CVolumeSerialNumber:
            return str(
                CVolumeSerialNumber)  # number is long type，has to be changed to str for comparing to content after.
        else:
            return 0

    # 使用DES加base64的形式加密
    # 考虑过使用M2Crypto和rsa，但是都因为在windows环境中糟糕的安装配置过程而放弃
    def DesEncrypt(self, str):
        k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
        EncryptStr = k.encrypt(str)
        # EncryptStr = binascii.unhexlify(k.encrypt(str))
        return base64.b64encode(EncryptStr)  # 转base64编码返回

    # des解码
    def DesDecrypt(self, str):
        k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
        DecryptStr = k.decrypt(str)
        # DecryptStr = a2b_hex(k.decrypt(str))
        print(DecryptStr)
        return DecryptStr

    # 获取注册码，验证成功后生成注册文件
    def regist(self):
        key = input('please input your register code: ')
        # 由于输入类似“12”这种不符合base64规则的字符串会引起异常，所以需要增加输入判断
        # while key
        if key:
            content = self.getCVolumeSerialNumber()
            key_decrypted = str(self.DesDecrypt(base64.b64decode(key)))
            if content != 0 and key_decrypted != 0:
                if content != key_decrypted:
                    print("wrong register code, please check and input your register code again:")
                    self.regist()
                elif content == key_decrypted:
                    print("register succeed.")
                    # 读写文件要加判断
                    with open('./register', 'w') as f:
                        f.write(key)
                        f.close()
                    return True
                else:
                    return False
            else:
                return False
        else:
            self.regist()
        return False

    def checkAuthored(self):
        content = self.getCVolumeSerialNumber()
        checkAuthoredResult = 0
        # 读写文件要加判断
        try:
            f = open('./register', 'r')
            if f:
                key = f.read()
                if key:
                    key_decrypted = self.DesDecrypt(base64.b64decode(key))
                    if key_decrypted:
                        if key_decrypted == content:
                            checkAuthoredResult = 1
                        else:
                            checkAuthoredResult = -1
                    else:
                        checkAuthoredResult = -2
                else:
                    checkAuthoredResult = -3
            else:
                self.regist()
        except IOError:
            print(IOError)
        print(checkAuthoredResult)
        return checkAuthoredResult


if __name__ == '__main__':
    reg = register()
    # reg.checkAuthored()
    reg.regist()
