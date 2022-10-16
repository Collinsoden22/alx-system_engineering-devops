#Kill 'killmenow' process
#!/usr/bin/pup
exec{'killmenow':
	command => 'pkill killmenow',
	provider => 'shell'
}
