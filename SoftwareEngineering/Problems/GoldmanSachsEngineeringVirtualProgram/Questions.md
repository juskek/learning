# Tracker
## Uncracked

## Cracked
### Dict Attack: rockyou.txt
hashcat -m 0 -a 0 -o cracked.txt PasswordHashes.txt dicts/rockyou.txt
- MD5 dictionary attack
```
edi_tesla89:6c569aabbf7775ef8fc570e228c16b98:password!
liveltekah:3f230640b78d7e71ac5514e57935eb69:qazxsw
experthead:e10adc3949ba59abbe56e057f20f883e:123456
interestec:25f9e794323b453885f5181f1b624d0b:123456789
reallychel:5f4dcc3b5aa765d61d8327deb882cf99:password
eatingcake1994:fcea920f7412b5da7be0cf42b8c93759:1234567
bookma:25d55ad283aa400af464c76d713c07ad:12345678
popularkiya7:e99a18c428cb38d5f260853678922e03:abc123
ortspoon:d8578edf8458ce06fbc5bb76a58c5ca4:qwerty
simmson56:96e79218965eb72c92a549dd5a330112:111111
heroanhart:7c6a180b36896a0a8c02787eeafb0e4c:password1
johnwick007:f6a0cb102c62879d397b12b62c092c06:bluered
blikimore:917eb5e9d6d6bca820922a0c6f7cc28b:Pa$$word1
```
FINDINGS: 
- minimum length is 6
- max length so far is 9
- uppercase is not required
- numbers are not required
### Dict Attack: top10mil.txt
hashcat -m 0 -a 0 -o cracked.txt PasswordHashes.txt dicts/top10mil.txt
NO NEW CRACKS

### Mask Attack: lowercase


6: hashcat -m 0 -a 3 PasswordHashes.txt "?l?l?l?l?l?l"
7: hashcat -m 0 -a 3 PasswordHashes.txt "?l?l?l?l?l?l?l"
8: hashcat -m 0 -a 3 PasswordHashes.txt "?l?l?l?l?l?l?l?l"
9: hashcat -m 0 -a 3 PasswordHashes.txt "?l?l?l?l?l?l?l?l?l"
NO NEW CRACKS

### Mask Attack: uppercase
6: hashcat -m 0 -a 3 PasswordHashes.txt "?u?u?u?u?u?u"
7: hashcat -m 0 -a 3 PasswordHashes.txt "?u?u?u?u?u?u"
8: hashcat -m 0 -a 3 PasswordHashes.txt "?u?u?u?u?u?u"
9: hashcat -m 0 -a 3 PasswordHashes.txt "?u?u?u?u?u?u"
NO NEW CRACKS

### Mask Attack: x lower + y numbers
x4y2: hashcat -m 0 -a 3 PasswordHashes.txt "?l?l?l?l?d?d"
x5y2: hashcat -m 0 -a 3 PasswordHashes.txt "?l?l?l?l?l?d?d"
NO NEW CRACKS

x6y2: hashcat -m 0 -a 3 PasswordHashes.txt "?l?l?l?l?l?l?d?d"
```
moodie:8d763385e0476ae208f21bc63956f748:moodie00
```
FINDINGS: 
- password for this user is the username and two numbers

### Hybrid Dictionary + Mask Attack: username + y numbers
usernameYY: hashcat -m 0 PasswordHashes.txt -a 6 lowercaseUsernames.txt "?d?d"
usernameYYYY: hashcat -m 0 PasswordHashes.txt -a 6 lowercaseUsernames.txt "?d?d?d?d"

UsernameYY: hashcat -m 0 PasswordHashes.txt -a 6 titlecaseUsernames.txt "?d?d"
```
spuffyffet:1f5c5683982d7c3814d4d9e6d749b21e:Spuffyffet12
```
UsernameYYYY: hashcat -m 0 PasswordHashes.txt -a 6 titlecaseUsernames.txt "?d?d?d?d"
```
oranolio:16ced47d3fc931483e24933665cded6d:Oranolio1994
```
FINDINGS:
- These passwords are just the username titlecased with two/four additional numbers, which is a common number of digits to add to represent some year

### Rule Based: Titlecased username
Username: hashcat -m 0 PasswordHashes.txt -a 0 titlecaseUsernames.txt
```
flamesbria2001:9b3b269ad0a208090309f091b3aba9db:Flamesbria2001
```

### Replacing characters with symbols
Common substitutions:
$, S or 5 for s
1, I or ! for i
1 or ! for l
@ or A for a
7 or T for t
3 or E for e
9, G or 6 for g
0 or O for o
8 or B for b

Remaining usernames: bandalls, nabox

- Replace usernames
hashcat -m 0 PasswordHashes.txt -a 0 lowercaseUsernames.txt -r rules.txt
usernameReplaceds5: ss5
usernameReplacedS$: sS$
usernameReplaceda@: sa@
usernameReplacedaA: saA
usernameReplacedo0: so0
usernameReplacedoO: soO
usernameReplacedb8: sb8
usernameReplacedbB: sbB
usernameReplacedl1: sl1

Usernamereplaceds5: ss5 c
Usernamereplaceds$: sS$ c
Usernamereplaceda@: sa@ c
Usernamereplacedaa: saA c
Usernamereplacedo0: so0 c
Usernamereplacedoo: soO c
Usernamereplacedb8: sb8 c
Usernamereplacedbb: sbB c
Usernamereplacedl1: sl1 c
```
bandalls:bdda5f03128bcbdfa78d8934529048cf:Banda11s
```
### Dive Ruleset
hashcat -m 0 PasswordHashes.txt -a 0 lowercaseUsernames.txt -r rules/dive.rule
NO NEW CRACKS

### NSAKEY Ruleset
hashcat -m 0 PasswordHashes.txt -a 0 lowercaseUsernames.txt -r rules/nsakey.rule
NO NEW CRACKS

### Mask: Brute Force all characters
6: hashcat -m 0 -a 3 PasswordHashes.txt "?a?a?a?a?a?a"
7: hashcat -m 0 -a 3 PasswordHashes.txt "?a?a?a?a?a?a?a"
```
nabox:defebde7b6ab6f24d5824682a16c3ae4:nAbox!1
```
# Email Memo 
Dear ____,

As requested, I have reviewed the security level of passwords from the leaked database and have arrived at the following findings:
- Hashing Algorithm: MD5
- Cracked Passwords: 19/19
- 

# What type of hashing algorithm was used to protect passwords?
Each of the hashes are 32 characters, which leads me to suspect that the hashing algorithm is the commonly used MD5, since it is a 128-bit hash function which produces 32 hexadecimal digits. However, other algorithms which produce 32 digit hashes include MD2, MD4, haval

It should be noted that a 32 character hash does not indicate the use of the aforementioned algorithms, since the hash 
-  could be produced by a longer encryption algorithm but stored in a 32-character field, or 
-  could be produced by concatenating two or more shorter hashing functions.

To determine whether an MD5 algorithm was used, HashCat was used to brute force commonly used passwords against the provided hashes. The following attacks were used to crack

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