iperf.exe -c sptest.local -P 20 -y C » %computername:~0,6% && pscp.exe -q -pw password %computername:~0,6% iperf@speedtest.local:/var/www/html/in
