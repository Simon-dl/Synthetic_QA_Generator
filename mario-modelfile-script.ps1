
    try {
        ollama show pls-work:latest --modelfile > mario-modelfile
        Write-Host "Successfully created mario-modelfile"
    } catch {
        Write-Error "Failed to create modelfile: $_"
        exit 1
    }
    