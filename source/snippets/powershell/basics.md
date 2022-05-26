# Basic Powershell Snippets

## Variables

### Assign variable

```powershell

$var_name = "this"

```

## Environment

### Set environment variable

```powershell

$env:VAR_NAME = 'variable'

```

### Get all environment variables

```powershell
dir env:
```

## Calling

### Call Operator

```powershell
& 'c:\Path\To\target.exe'
```
