foreach ($i in (gdr -PSProvider 'FileSystem')){
    Set-Location -Path $i.Root;
    Get-ChildItem . -Attributes Directory+Hidden -ErrorAction SilentlyContinue -Filter ".git" -Recurse | % { Write-Host $_.parent.FullName }
}