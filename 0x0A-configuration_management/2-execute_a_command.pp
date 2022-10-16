#Kill 'killmenow' process
exec{'killmenow':
	command => 'pkill killmenow',
	provider => 'shell'
}
