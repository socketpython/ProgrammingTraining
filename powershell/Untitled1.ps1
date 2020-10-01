$processes = Get-Process -Name *win*

foreach ($process in $processes){
    $name = $process.Name
    $cpu = $process.CPU
    if ($cpu -gt 3){
        write-host "The process '$name' is a cpu eater"
    }
    else{
        write-host "The process '$name' is not a cpu eater"
    }
}