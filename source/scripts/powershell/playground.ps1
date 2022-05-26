$SCRIPT_FOLDER = $PSScriptRoot


$SCRIPT_FOLDER



Get-Module -ListAvailable |

ForEach-Object { “`r`n## module name: $_”; “`r`n”; Get-Command -Module $_.name -CommandType cmdlet, function | Select-Object name } | Out-File -FilePath 'blah.md'