# Executes a bash command
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin'],
  returns => [0, 1], # Allow exit code 1
}
