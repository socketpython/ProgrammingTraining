$ip = Read-Host "Enter ip address"
$user_name = Read-Host "Enter username"
ssh $ip -l $user_name