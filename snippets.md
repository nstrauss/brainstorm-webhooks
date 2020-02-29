# If This Then That: Automation with Webhooks
https://docs.google.com/presentation/d/1O-OFsXlI9u1Z7XuiNpsD0yM7uKMFl90qgdADgvHcFBg/edit?usp=sharing


# Mac/Linux
### Example App Store API GET
`curl "https://itunes.apple.com/us/lookup?id=507874739" | python -m json.tool`

### Get a specific value from JSON
`curl "https://itunes.apple.com/us/lookup?id=507874739" | python -c 'import sys, json; print json.load(sys.stdin)["results"][0]["version"]'`

### Send a webhook
`curl https://hooks.zapier.com/hooks/catch/1234567/abcdefg/ -X POST -d @./webhook_examples/hook_example1.json`


# Windows PowerShell
### Example App Store API GET
`(Invoke-WebRequest -Uri "https://itunes.apple.com/us/lookup?id=507874739").Content | ConvertFrom-Json | ConvertTo-Json`

### Get a specific value from JSON
`(Invoke-WebRequest -Uri "https://itunes.apple.com/us/lookup?id=507874739").Content | ConvertFrom-Json | select -expand results | Select-Object -ExpandProperty version`

### Send a webhook
 `Invoke-RestMethod "https://hooks.zapier.com/hooks/catch/1234567/abcdefg/" -Method Post -Body C:\path\to\brainstorm\hook_example1.json`
