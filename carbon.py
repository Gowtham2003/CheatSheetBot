import urllib

def carbonize(code,chat_id):
    #Todo: Code needs formatting fix!
    code = urllib.parse.quote_plus(code)
    api_url = f"https://carbonnowsh.herokuapp.com/?code={code}&theme=darcula&backgroundColor=6E7AF2" 
    filename = str(chat_id) + "_code_snap.png"
    try:
        urllib.request.urlretrieve(api_url, filename=filename)
    except Exception:
        return None
    return filename