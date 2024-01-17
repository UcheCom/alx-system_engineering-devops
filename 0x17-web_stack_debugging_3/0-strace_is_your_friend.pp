# This Puppet manifest fixes bad `phpp` extensions to 
# `php` in the WordPress file `wp-settings.php`.

exec { 'fix-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin/']
}
