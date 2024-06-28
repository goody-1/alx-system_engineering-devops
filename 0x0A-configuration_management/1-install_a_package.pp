# Install flask package from pip3

# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Use exec resource to install Flask with pip3
exec { 'install flask 2.1.0':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/bin/pip3 show flask | grep "Version: 2.1.0"',
  require => Package['python3-pip'],
}
