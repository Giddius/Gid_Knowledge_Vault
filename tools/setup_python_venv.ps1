#Requires -RunAsAdministrator

$repoRootFolder = Split-Path $PSScriptRoot -Parent
$requirementsFile = Join-Path -Path $repoRootFolder -ChildPath "tools\python_requirements.txt"
$requirementsFileDev = Join-Path -Path $repoRootFolder -ChildPath "tools\python_dev_requirements.txt"
$venvDir = Join-Path -Path $repoRootFolder -ChildPath ".venv"
$venvExecutable = Join-Path -Path $venvDir -ChildPath "Scripts\python.exe"

$rawBasePythonDir = ((python -c "import sys;print(sys.base_prefix)") | Out-String).Trim()
$basePythonDir = Resolve-Path $rawBasePythonDir
$BasePythonExe = Join-Path -Path $basePythonDir -ChildPath "python.exe"



Push-Location $repoRootFolder

Write-Host $(`
    "`n"+`
    "Upgrading system pip" +`
    "`n--------------------`n" )`
    -ForegroundColor Yellow

& $BasePythonExe.Trim() -m pip install --upgrade pip



Write-Host $(`
    "`n" +`
    "creating fresh venv in "        +`
    $venvDir.Trim() +`
    "`n-----------------------------------------------------------------------------`n"       )`
    -ForegroundColor Yellow


& $BasePythonExe.Trim() -m venv --clear --upgrade-deps $venvDir

if ($? -eq $False) {exit}

& $venvExecutable -m pip install --upgrade wheel
& $venvExecutable -m pip install --upgrade PEP517
& $venvExecutable -m pip install --upgrade python-dotenv
Write-Host $(`
    "`n"+`
    "Installing Dependencies from " +`
    $requirementsFile.Trim() +`
    "`n-----------------------------------------------------------------------------------------------`n" )`
    -ForegroundColor Yellow

& $venvExecutable -m pip install -r $requirementsFile
if ($? -eq $False) {exit}
Write-Host $(`
    "`n"+`
    "Installing DEV Dependencies from " +`
    $requirementsFileDev.Trim() +`
    "`n-----------------------------------------------------------------------------------------------`n" )`
    -ForegroundColor Yellow

& $venvExecutable -m pip install -r $requirementsFileDev
if ($? -eq $False) {exit}


Write-Host $(`
    "`n"+`
    "`n-----------------------------------------------------" +`
    "`n=====================================================`n" +`
    "                     Finished" +`
    "`n=====================================================`n" +`
    "-----------------------------------------------------`n" )`
    -ForegroundColor Yellow
