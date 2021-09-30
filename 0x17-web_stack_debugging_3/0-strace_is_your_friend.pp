# Manifest to configure an Ubuntu server with nginx

exec  { 'update file':
    command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
    user     => 'root',
    provider => 'shell'
}
