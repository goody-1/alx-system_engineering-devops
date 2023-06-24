# make changes to configuration file
package { 'augeas-tools':
  ensure => installed,
}

augeas { 'Declare identity file':
  lens    => 'Ssh.lns',
  incl    => '/etc/ssh/ssh_config',
  changes => [
    'set Host/IdentityFile[.="~/.ssh/school"] "~/.ssh/school"',
  ],
  require => Package['augeas-tools'],
}

augeas { 'Turn off passwd auth':
  lens    => 'Ssh.lns',
  incl    => '/etc/ssh/ssh_config',
  changes => [
    'set Host/PasswordAuthentication "no"',
  ],
  require => Package['augeas-tools'],
}
