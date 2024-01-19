# Killing a process called killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}