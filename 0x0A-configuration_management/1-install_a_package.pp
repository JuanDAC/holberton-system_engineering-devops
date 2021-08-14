# Packege puppet-lint installed with version 2.1.1
package { 'puppet_lint':
  ensure   => '2.1.1',
  name     => 'puppet-lint',
  provider => 'gem'
}
