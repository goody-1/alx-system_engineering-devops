# Kill a process 'killmenow' with pkill
exec { 'killmenow_process':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
}
