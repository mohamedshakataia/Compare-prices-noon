import requests
import csv
import psycopg2
import json
import time

page_number=1
url = "https://www.noon.com/_svc/catalog/api/search"
headers = {
  'authority': 'www.noon.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
  'x-locale': 'en-eg',
  'x-content': 'mobile',
  'x-mp': 'noon',
  'x-platform': 'web',
  'x-cms': 'v2',
  'content-type': 'application/json',
  'accept': 'application/json, text/plain, */*',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
  'origin': 'https://www.noon.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.noon.com/egypt-en/electronics-and-mobiles/',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'AKA_A2=A; visitor_id=da915c6a-dff6-47c4-8b6e-d322eff07873; _gcl_au=1.1.991456458.1610798477; _ga=GA1.2.1745773522.1610798478; _gid=GA1.2.1502985728.1610798478; _scid=6a2344b7-09fe-429c-b062-4a6005538759; _fbp=fb.1.1610798477868.1693100741; _sctr=1|1610748000000; __zlcmid=12Bjjtre7IQmAYx; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lKbFpqQXpZalF3TnpOaE1EUTBNek16WWpNd05XSTJPV014WTJVME0yVmlOaUlzSW1saGRDSTZNVFl4TURjNU9EUTNObjAuN2dQLU1OeU8ycUhQb3doc3ZhQlVfV282NVVGLWJDdzFSS2hWM0laX0FKQSIsImlhdCI6MTYxMDc5OTY5NH0.SyfspvofHfhNP2_FRR10tmry79xDuSnivuxVnPcM8LQ; _nsc=nsv1.public.eyJzdGlkIjoiMzM4ZjNlODQtZjY1Ny00YTYwLWFjY2YtN2MwYTNjNzlkYjlkIiwic2lkIjoiZWYwM2I0MDczYTA0NDMzM2IzMDViNjljMWNlNDNlYjYiLCJpYXQiOjE2MTA3OTk2OTQsInZpZCI6ImRhOTE1YzZhLWRmZjYtNDdjNC04YjZlLWQzMjJlZmYwNzg3MyIsImhvbWVwYWdlIjp7fX0wQXk1UEw1ZnFZMG5VM05PT3JodHNwZXQzTi9oVVl3aTRxMFJxWHdOdDBJPQ.MQ; next-i18next=ar-EG; RT="z=1&dm=noon.com&si=hl3cputspth&ss=kjzntkse&sl=3&tt=7oa&obo=1&rl=1&nu=d41d8cd98f00b204e9800998ecf8427e&cl=tkq7"; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJM09HSTRNalUyWldNek9URTBaV1kyT0ROaVpHSXpPVEppWVRjMU1qazJOeUlzSW1saGRDSTZNVFl3TlRJd016VXdObjAuY0N2Y2htZjBCa1I2aXBJZW5BN3lMQ0xaRElVbmFLNzJ2SkpNcUdpV0JsMCIsImlhdCI6MTYxMDc5OTI4Nn0.PRi1VTECfaP-GQqeB3gpYuXhcIxlKZ9dHvXZYcsXQgM; _nsc=nsv1.public.eyJzdGlkIjoiZmQzY2EwODYtZjBlMi00NjY2LTg5MzgtOTE5M2JiY2FjYzEwIiwic2lkIjoiNzhiODI1NmVjMzkxNGVmNjgzYmRiMzkyYmE3NTI5NjciLCJpYXQiOjE2MTA3OTkyODYsInZpZCI6IjVjZjQ2NzYwLWQ3ZmMtNGRiYy1iYzhiLTM0ZTVkNzMwM2Y3MiIsImhvbWVwYWdlIjp7fX1aOWYwdVFNd3lrY3BGYnFvcjJ6ajA1R1RPM0d4RGszaUdoa2twN0JjZUFJPQ.MQ; next-i18next=ar-EG; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJM09HSTRNalUyWldNek9URTBaV1kyT0ROaVpHSXpPVEppWVRjMU1qazJOeUlzSW1saGRDSTZNVFl3TlRJd016VXdObjAuY0N2Y2htZjBCa1I2aXBJZW5BN3lMQ0xaRElVbmFLNzJ2SkpNcUdpV0JsMCIsImlhdCI6MTYxMDc5OTMxN30.oAoPDvGWyb63l7TVBsmsSZLkoWA3eQ-PFmhzsQH--zk'
}
def connn():
  conn = psycopg2.connect(database='Notify', user='postgres', password='1999', host='localhost', port='5432')
  cur = conn.cursor()
  return(conn,cur)
def var(*t):
    for z in t:
        z=z['sku']
    
def data(*n):
  for l in n:
    v=l['offer_code'],l['sku'] ,l['name'],l['is_buyable'],l['price']
    conn,cur=connn()       
    cur.execute("INSERT INTO Data_Noon(NoonID,sku,title,active,lastprice) VALUES (%s , %s,%s,%s,%s)",(v))
    conn.commit()  
a=True
while a :
    payload={"brand":[],"category":["electronics-and-mobiles"],"filterKey":[],"f":{},"sort":{"by":"popularity","dir":"desc"},"limit":150,"page":page_number}
    response = requests.request("POST", url, headers=headers, json=payload).json()
    a=response.get('hits')
    data(*a)
    var(*a)
    k=0
    for item in a:
        e=a[k]['sku']
        q=a[k]['offer_code']
        x=a[k]['name']
        print
        k+=1
#   q=time.sleep(3)
#   print(q)

    page_number+=1



url = "https://www.noon.com/_svc/reviews/fetch/v1/product-reviews/list"

payload="{\"catalogCode\":\"noon\",\"sku\":\"N40501389A\",\"lang\":null,\"ratings\":[1,2,3,4,5],\"provideBreakdown\":true,\"page\":1}"
headers = {
  'authority': 'www.noon.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
  'x-locale': 'en-eg',
  'x-content': 'mobile',
  'x-mp': 'noon',
  'x-platform': 'web',
  'x-cms': 'v2',
  'content-type': 'application/json',
  'accept': 'application/json, text/plain, */*',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
  'origin': 'https://www.noon.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.noon.com/egypt-en/poco-x3-dual-sim-shadow-gray-nfc-6gb-ram-64gb-4g-lte/N40501389A/p?o=b5e2b2f5b163988f',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'visitor_id=da915c6a-dff6-47c4-8b6e-d322eff07873; _gcl_au=1.1.991456458.1610798477; _ga=GA1.2.1745773522.1610798478; _gid=GA1.2.1502985728.1610798478; _scid=6a2344b7-09fe-429c-b062-4a6005538759; _fbp=fb.1.1610798477868.1693100741; _sctr=1|1610748000000; __zlcmid=12Bjjtre7IQmAYx; AKA_A2=A; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lKbFpqQXpZalF3TnpOaE1EUTBNek16WWpNd05XSTJPV014WTJVME0yVmlOaUlzSW1saGRDSTZNVFl4TURjNU9EUTNObjAuN2dQLU1OeU8ycUhQb3doc3ZhQlVfV282NVVGLWJDdzFSS2hWM0laX0FKQSIsImlhdCI6MTYxMDk5ODU3N30.lA9ysRLexKNQWd5nr1rnUP8lShqxkUSwfBLPNsV2OBg; _nsc=nsv1.public.eyJzdGlkIjoiMTJkYWMwZDctZGIzNi00Njg5LThhNTgtMGQxNTFiNzhlYjQ1Iiwic2lkIjoiZWYwM2I0MDczYTA0NDMzM2IzMDViNjljMWNlNDNlYjYiLCJpYXQiOjE2MTA5OTg1NzcsInZpZCI6ImRhOTE1YzZhLWRmZjYtNDdjNC04YjZlLWQzMjJlZmYwNzg3MyIsImhvbWVwYWdlIjp7fX1lV3cwU1FZOFRsNHVzRy9LcmpQNUFvTUFPYXQwRFMwcGpocVE5a1FkRmdnPQ.MQ; _gcl_aw=GCL.1610998591.CjwKCAiAgJWABhArEiwAmNVTB8bTM2FmNYg9R7wqPgqbdsAwkntoI9umO1Og5lkUr72tulbPJKorUhoCV5cQAvD_BwE; _gac_UA-84507530-14=1.1610998596.CjwKCAiAgJWABhArEiwAmNVTB8bTM2FmNYg9R7wqPgqbdsAwkntoI9umO1Og5lkUr72tulbPJKorUhoCV5cQAvD_BwE; next-i18next=ar-EG; _gat_UA-84507530-14=1; RT="z=1&dm=noon.com&si=6fe91e87-eab2-4348-a142-410def3f6200&ss=kk2yzexr&sl=0&tt=0&nu=3982475b332e3e1b0003d2efc491f6a6&cl=ltg"; next-i18next=ar-EG; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJM09HSTRNalUyWldNek9URTBaV1kyT0ROaVpHSXpPVEppWVRjMU1qazJOeUlzSW1saGRDSTZNVFl3TlRJd016VXdObjAuY0N2Y2htZjBCa1I2aXBJZW5BN3lMQ0xaRElVbmFLNzJ2SkpNcUdpV0JsMCIsImlhdCI6MTYxMDc5OTMxN30.oAoPDvGWyb63l7TVBsmsSZLkoWA3eQ-PFmhzsQH--zk; _nsc=nsv1.public.eyJzdGlkIjoiNzQ3Nzg5N2UtMWVkOC00MWZkLWEwZGQtZTZkNTIzOTVhMWE4Iiwic2lkIjoiZWYwM2I0MDczYTA0NDMzM2IzMDViNjljMWNlNDNlYjYiLCJpYXQiOjE2MTA5OTg1NTYsInZpZCI6ImRhOTE1YzZhLWRmZjYtNDdjNC04YjZlLWQzMjJlZmYwNzg3MyIsImhvbWVwYWdlIjp7fX1jNXY3c1I3aVVnWDFLNjdKOVB0VU16cnFSOUJlRVVFbEFmMi8weDNWeGcwPQ.MQ; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJM09HSTRNalUyWldNek9URTBaV1kyT0ROaVpHSXpPVEppWVRjMU1qazJOeUlzSW1saGRDSTZNVFl3TlRJd016VXdObjAuY0N2Y2htZjBCa1I2aXBJZW5BN3lMQ0xaRElVbmFLNzJ2SkpNcUdpV0JsMCIsImlhdCI6MTYxMDk5ODcwMn0.kJs6N_-eZdsIsUHb6y8DbCd9h5whk9r0SmfyJDkpih4'
}

response = requests.request("POST", url, headers=headers, data=payload).json()
a=response['summary']['rating']
print(a)



# payload={"catalogCode":"noon","sku":"N40501389A","lang":null,"ratings":[1,2,3,4,5],"provideBreakdown":true,"page":1}


































        