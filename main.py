import requests
from twilio.rest import Client

# stock = "TSLA"
# comp = "Tesla Inc"
stock = "SNAP"
comp = "Snap Inc"

stkend = "https://www.alphavantage.co/query"
nsend =  "https://newsapi.org/v2/everything"

apik = "JVPEJERSSI5SW0TU"
nsapk = "ab53b3ce8d4d415fb8e2aa0105dcac90"
tacid = "AC405565638eb21752d664f91e7c1c16ce"
tactkn = "3685d4c70f1f0aa0cef968c2c586d4d2"

stkpm = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock,
    "apikey": apik
}
rsp = requests.get(url=stkend, params=stkpm)
dat = rsp.json()["Time Series (Daily)"]
dlst = [v for (k,v) in dat.items()]
ycls = dlst[0]["4. close"]
print(ycls)
dbyc = dlst[1]["4. close"]
print(dbyc)
# dif = abs(float(ycls) - float(dbyc))
dif = float(ycls) - float(dbyc)
up = None
if dif > 0:
   up = "🔺"
else:
    up = "🔻"

per = round((dif / float(ycls)) * 100, 2)
print(per)
if abs(per) > 0:
    nspms = {
        "apiKey": nsapk,
        "qInTitle": comp,
    }
    nsrsp = requests.get(url=nsend,params=nspms)
    art = nsrsp.json()["articles"][:3]
    art1 = [f"{stock}: {up}{per}%\n\nHeadlines: {i['title']}. \n\nBrief: {i['description']}" for i in art]
    # print(art1)
    clnt = Client(tacid, tactkn)
    for q in art1:
        msg = clnt.messages.create(
            body=q,
            from_='+19256432125',
            to='+919491654127'
        )
        print(msg.status)