### GEO IP FreeAPI
Is a simple API develop in PYTHON and Flask, to integration in LocationIQ for free user :)

### How to teste API

Endpoint demo Request GET:

```
https://geoip.contrateumdev.com.br/api/geoip?ip=177.79.48.86
```

Response SUCCESS:

```json
{
    "ip": "177.79.48.86",
    "hostname": "ip-177-79-48-86.user.vivozap.com.br",
    "city": "Pune",
    "region": "Maharashtra",
    "country": "IN",
    "loc": "18.5196,73.8554",
    "org": "AS26599 TELEFÔNICA BRASIL S.A",
    "postal": "411005",
    "timezone": "Asia/Kolkata",
    "readme": "https://ipinfo.io/missingauth"
}
```
### How to consume API in $.POST Jquery

```javascript
function getData()
{
    $.post({
        method: 'GET',
        url: 'https://geoip.contrateumdev.com.br/api/geoip?ip=177.79.48.86',
        success: function(resultado, status, xhr) {
            if (resultado) {
                console.log(resultado)
            }else{
                console.log(resultado)
            }
        },
        error: function(data) {
            console.log(data.error)
        }
    })
}
```
