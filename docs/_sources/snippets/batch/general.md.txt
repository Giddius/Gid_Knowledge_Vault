# General Batch/cmd Snippets


## get clipboard data

```batch
for /f "eol=; tokens=*" %%I in ('powershell Get-Clipboard') do set CLIPBOARD_TEXT=%%I
```