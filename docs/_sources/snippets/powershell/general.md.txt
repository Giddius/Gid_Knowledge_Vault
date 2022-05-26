# General Powershell Snippets

## Get all local Git Repo Paths

```powershell
Set-Location -Path D:\; Get-ChildItem . -Attributes Directory+Hidden -ErrorAction SilentlyContinue -Filter ".git" -Recurse | % { Write-Host $_.FullName -replace"\\.git" }
```

## Folder of Script itself

```powershell
$PSScriptRoot
```
