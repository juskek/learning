# What type of hashing algorithm was used to protect passwords?
Each of the hashes are 32 characters, which leads me to suspect that the hashing algorithm is the commonly used MD5, since it is a 128-bit hash function which produces 32 hexadecimal digits. However, other algorithms which produce 32 digit hashes include MD2, MD4, haval

It should be noted that a 32 character hash does not indicate the use of the aforementioned algorithms, since the hash 
-  could be produced by a longer encryption algorithm but stored in a 32-character field, or 
-  could be produced by concatenating two or more shorter hashing functions.

To determine whether an MD5 algorithm was used, HashCat was used to brute force commonly used passwords against the provided hashes. The following stages were used:

Stage 1
- Hash: MD5
- Attack: Dictionary
  - Dictionary used was a wordlist of over 14 million passwords from the RockYou exposure in 2009
- Cracked: 13/19
```
6c569aabbf7775ef8fc570e228c16b98:password!
3f230640b78d7e71ac5514e57935eb69:qazxsw
e10adc3949ba59abbe56e057f20f883e:123456
25f9e794323b453885f5181f1b624d0b:123456789
5f4dcc3b5aa765d61d8327deb882cf99:password
fcea920f7412b5da7be0cf42b8c93759:1234567
25d55ad283aa400af464c76d713c07ad:12345678
e99a18c428cb38d5f260853678922e03:abc123
d8578edf8458ce06fbc5bb76a58c5ca4:qwerty
96e79218965eb72c92a549dd5a330112:111111
7c6a180b36896a0a8c02787eeafb0e4c:password1
f6a0cb102c62879d397b12b62c092c06:bluered
917eb5e9d6d6bca820922a0c6f7cc28b:Pa$$word1
```
- Remarks:
  - This confirms that the hashing algorithm used was MD5. A majority of the passwords were captured
Stage 2
- Hash: MD5
- Attack: 

# What level of protection does the mechanism offer for passwords?
# What controls could be implemented to make cracking much harder for the hacker in the event of a password database leaking again?
# What can you tell about the organization’s password policy (e.g. password length, key space, etc.)?
# What would you change in the password policy to make breaking the passwords harder? 