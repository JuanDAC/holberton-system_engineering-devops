# user limit, configuration

exec { 'fix hard and soft':
  command  => 'sed -i "56,57d" /etc/security/limits.conf',
  provider => 'shell'
}
