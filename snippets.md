# Mac/Linux
### Example App Store API GET
`curl "https://itunes.apple.com/us/lookup?id=507874739" | python -m json.tool`

### Get a specific value from JSON
`curl "https://itunes.apple.com/us/lookup?id=507874739" | python -c 'import sys, json; print json.load(sys.stdin)["results"][0]["version"]'`

### Send a webhook
`curl https://hooks.zapier.com/hooks/catch/1234567/abcdefg/ -X POST -d @/Users/nstrauss/Documents/hook_example.json`


# Windows PowerShell
### Example App Store API GET
`(Invoke-WebRequest -Uri "https://itunes.apple.com/us/lookup?id=507874739").Content | ConvertFrom-Json | ConvertTo-Json`

### Get a specific value from JSON
` (Invoke-WebRequest -Uri "https://itunes.apple.com/us/lookup?id=507874739").Content | ConvertFrom-Json | select -expand results | select version`

### Send a webhook
`Invoke-WebRequest -Uri 'https://hooks.zapier.com/hooks/catch/1234567/abcdefg/' ‑Method Post -Body $httpBody`