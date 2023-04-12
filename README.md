# Blockchain-HW1
---

This is my first assignment at Blockchain course.

I choose to implement **RSA** algorithm in Python using rsa library. 

With this script you can easily **generate** keypair, **sign** and **verify** the content

# How to use

`pip install rsa`

```
python main.py generate directory_name
python main.py file_to_sign.txt directory_name/private_key.pem 
python main.py file_to_verify.txt directory_name/public_key.pem file_to_verify.txt.sig
```
