```bash 
function prompt {
    # Get current location
    $currentPath = (Get-Location).Path

    # Replace home directory with "~"
    $shortPath = $currentPath -replace [regex]::Escape($HOME), "~"

    # Optionally show only last folder
    $shortPath = Split-Path $shortPath -Leaf

    # Return custom prompt
    "PS $shortPath> "
}

```