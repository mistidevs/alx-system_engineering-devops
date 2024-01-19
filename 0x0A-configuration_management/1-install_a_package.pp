# Installing flask the pip3 package
package { 'flask':
  ensure   => 'installed',
  provider => 'pip3',
}