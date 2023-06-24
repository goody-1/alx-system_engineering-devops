# make changes to configuration file, use private key
include stdlib

file_line { 'Declare identity file':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'IdentityFile ~/.ssh/holberton',
}

file_line { 'Turn off Password Auth':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'PasswordAuthentication no',
}
