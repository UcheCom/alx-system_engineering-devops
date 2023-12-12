# This installs Nginx and custom HTTP response headers

exec { '/usr/bin/env apt-get -y update' : }
-> package { 'nginx':
  ensure => installed,
}

-> file_line { 'add header':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  line   => '\tadd_header X-served-By ${hostname};',
  after  => 'server_name _;',
}

-> file { '/var/www/html/index.html':
  content => 'Holberton School!',
}

-> service { 'nginx':
  ensure  => running,
}

exec {'restart Nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
