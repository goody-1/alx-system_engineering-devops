# Kill a process 'killmenowing' with pkill
exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => '/usr/bin:/bin',
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}
