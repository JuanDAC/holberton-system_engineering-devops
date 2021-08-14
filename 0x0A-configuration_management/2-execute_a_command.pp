# To kill a process named 'killmenow'
exec { 'hasta_la_vista_baby':
  path    => '/usr/bin/',
  command => 'pkill -f killmenow'
}
