# Script to increase server requests limit.

file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 4100'\n",
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
