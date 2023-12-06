# This installs Nginx and custom HTTP response headers

package { 'nginx':
  ensure => installed,
}

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'server_name _;',
  line   => '\tadd_header X-served-By ${hostname};',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
}
