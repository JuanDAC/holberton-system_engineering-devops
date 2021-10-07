# Fixing the number of failed requests

service {'nginx':
  enable => true
  ensure => 'running',
}

exec { 'fix nginx':
  command  => 'sed -i "5 s/[[:digit:]]\{1,\}/$(ulimit -Hn)/" /etc/default/nginx',
  provider => 'shell'
  notify   => Service['nginx'],
}
