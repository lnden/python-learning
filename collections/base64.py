# ase64适用于小段内容的编码，比如数字证书签名、Cookie的内容等.
# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：

import base64
print(base64.b64encode(b'binary\x00string'))