#!/usr/bin/env bash
# Making changes to configuration file using Puppet

file { '/etc/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",

}
