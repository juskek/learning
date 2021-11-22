- [1. SYNTAX](#1-syntax)
- [2. mv](#2-mv)
- [3. mkdir](#3-mkdir)
- [4. touch](#4-touch)
- [5. cp](#5-cp)
- [6. rm](#6-rm)
- [7. cd](#7-cd)
- [8. code (VSCODE)](#8-code-vscode)
- [9. nano](#9-nano)
- [sudo](#sudo)
- [zsh](#zsh)

# 1. SYNTAX
- Present working directory: .
- Parent directory: ..
- Home directory: ~
- Root directory: /
- Previous directory: -

# 2. mv
- Move file: mv FileName ~/TargetDirectory
- Move directory: mv -R DirName ~/TargetDirectory
- Rename file/directory: mv OldName NewName

# 3. mkdir
- Create directory: mkdir DirName

# 4. touch
- Create file: touch FileName

# 5. cp
- Copy files: cp FileName
- Copy directory: cp -r DirName

# 6. rm
- Remove files: rm FileName
- Remove directory: rm -r DirName

# 7. cd
- Go to root: 

# 8. code (VSCODE)
- Open pwd in active window: code -a .
- Open pwd while reusing window: code -r .

# 9. nano
- 

# sudo
- super user do (root command privileges)


# zsh
- Rerun init and refresh zsh: exec zsh
- Adding environment to path:
  1. Navigate to home directory: `cd ~`
  2. Edit resource file: `nano .zshrc`
  3. Add environment: `export PATH=$PATH:<environmentPath>`
  4. Check if environment has been added correctly: `echo $PATH`