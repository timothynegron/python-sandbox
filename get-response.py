def getDataFromAPI(keys):

    conn = http.client.HTTPSConnection("API.com name here")
    payload = ''
    headers = {
        'accesstokenkey': keys[0],
        'accesstokensecret': keys[1]
    }
    
    # GetEventRegistrant (WORKS)
    conn.request("GET", "URL HERE", payload, headers)
    
    res = conn.getresponse()
    
    return res.read()