# This creates a file named school
file { 'school':
  ensure  => present,
  path    => '/tmp/school',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744'
}
