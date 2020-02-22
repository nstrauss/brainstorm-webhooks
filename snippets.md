# Example App Store API GET
### Mac/Linux
`curl "https://itunes.apple.com/us/lookup?id=507874739" | python -m json.tool`

### Windows PowerShell
`(Invoke-WebRequest -Uri "https://itunes.apple.com/us/lookup?id=507874739").Content | ConvertFrom-Json | ConvertTo-Json`


# Send a webhook using curl
### Mac/Linux
`curl https://hooks.zapier.com/hooks/catch/1234567/abcdefg/ -X POST -d @/Users/nstrauss/Documents/hook_example.json`


### Windows PowerShell
`Invoke-WebRequest -Uri 'https://hooks.zapier.com/hooks/catch/1234567/abcdefg/' ‑Method Post -Body $httpBody`