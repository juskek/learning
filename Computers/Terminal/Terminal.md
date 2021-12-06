- [1. Shell](#1-shell)
  - [1.1. sh: Bourne Shell](#11-sh-bourne-shell)
  - [1.2. bash: Bourne Again Shell](#12-bash-bourne-again-shell)
  - [1.3. zsh: Z shell](#13-zsh-z-shell)
- [2. Package Managers](#2-package-managers)
  - [2.1. Binary (Compiled Apps)](#21-binary-compiled-apps)
    - [2.2.1. homebrew (MacOS)](#221-homebrew-macos)
    - [](#)
  - [2.2. Source (Uncompiled Apps)](#22-source-uncompiled-apps)
  - [2.3 Application-Level](#23-application-level)
    - [nvm (Node.js)](#nvm-nodejs)
    - [npm (Node.js, JavaScript)](#npm-nodejs-javascript)
      - [npx](#npx)
    - [pip (Python, PyPI)](#pip-python-pypi)
    - [conda (Python, R)](#conda-python-r)
    - [2.2.2. yum](#222-yum)
    - [2.2.3. apt-get](#223-apt-get)
    - [2.2.4. choco](#224-choco)
    - [2.2.5. emerge](#225-emerge)
    - [2.2.6. wget](#226-wget)
- [3. File Retriever](#3-file-retriever)
  - [3.1. wget](#31-wget)
- [Data Transfer](#data-transfer)
  - [curl](#curl)
  - [wget](#wget)

# 1. Shell
- Command interpreter that executes other programs
- 


## 1.1. sh: Bourne Shell

## 1.2. bash: Bourne Again Shell

## 1.3. zsh: Z shell
- Extended version of sh

# 2. Package Managers

## 2.1. Binary (Compiled Apps)
### 2.2.1. homebrew (MacOS)


### 

## 2.2. Source (Uncompiled Apps)

## 2.3 Application-Level
### nvm (Node.js)
- Node version manager
- Installed per user
- Invoked per shell
  - run every time new shell is created `nvm install <version>` or `nvm use <version>`
### npm (Node.js, JavaScript)
- Node package manager
- Deps downloaded and put into node_modules folder 
  - Project specific 
  - @types folder provides TS support for JS libs

#### npx
- Node package execute
  - Run packages without having to install them locally/globally
- Preinstalled with npm
- 
### pip (Python, PyPI)
### conda (Python, R)
### 2.2.2. yum

### 2.2.3. apt-get

### 2.2.4. choco

### 2.2.5. emerge

### 2.2.6. wget

# 3. File Retriever
## 3.1. wget
- Retrieving files using HTTP, HTTPS, FTP and FTPS

# Data Transfer
## curl
- client URL
- Supported protocols
  - FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, POP3, IMAP, SMTP, RTMP and RTSP
- Features
  - upload and sending
## wget
- www get
- recursive downloads
- supported protocols
  - HTTP, HTTPS and FTP
- Features
  - HTTP POST