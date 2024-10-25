from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_executor import Executor
import requests, random, string, re, uuid, time, os

app = Flask("perplexityApi")
executor = Executor(app)
CORS(app)


session = False
workerStatus = False

def sessionUpdate():
    global workerStatus
    workerStatus=True
    timeStopper=0
    if not session:
        createSession()
    while True:
        try:
            uidcontext = str(uuid.uuid4())
            uidfrontend = str(uuid.uuid4())
            uidvisit = re.search("pplx.visitor-id=(.*?);", cloudSolver()["cookie"]).group(1)
            url1 = f'https://www.perplexity.ai/socket.io/?EIO=4&transport=polling&t={rand(mode=1)}'
            r = session.get(f"{url1}{rand()}", headers=cloudSolver()).text
            sid = re.search("\"sid\":\"(.*?)\"", r).group(1)
            p = session.post(f"{url1}{rand()}&sid={sid}", data='40{"jwt":"anonymous-ask-user"}', headers=cloudSolver(newSolver=session.cookies.get_dict())).text
            p = session.post(f"{url1}{rand()}&sid={sid}", data='40{"jwt":"anonymous-ask-user"}', headers=cloudSolver(newSolver=session.cookies.get_dict())).text
            p = session.post(f"{url1}{rand()}&sid={sid}", data='4214["perplexity_ask","' + "buatkan pantun lucu satu aja" + '",{"version":"2.9","source":"mweb","attachments":[],"language":"id","timezone":"Asia/Makassar","search_focus":"internet","frontend_uuid":"' + uidfrontend + '","mode":"concise","is_related_query":false,"visitor_id":"' + uidvisit + '","frontend_context_uuid":"' + uidcontext + '","prompt_source":"user","query_source":"home","is_incognito":false,"time_from_first_type":13200}]\u001e42["analytics_event",{"version":"2.9","source":"mweb","event_name":"submit query","event_data":{"queryStr":"' + "buatkan pantun lucu satu aja" + '","queryParams":{"attachments":[],"language":"id","timezone":"Asia/Makassar","search_focus":"internet","frontend_uuid":"' + uidfrontend + '","mode":"concise","is_related_query":false,"visitor_id":"' + uidvisit + '","frontend_context_uuid":"' + uidcontext + '","prompt_source":"user","query_source":"home","is_incognito":false,"time_from_first_type":13200},"isFollowup":false,"submissionCount":1,"submissionType":"perplexity_ask","frontendUUID":"' + uidfrontend + '","submitTimestamp":' + str(int(time.time())) + ',"startFirstServerResponseMarker":{"eventTime":-1},"startLLMTokenMarker":{"eventTime":-1},"endStreamTimestamp":null,"finalizedTimestamp":null,"firstServerResponseReceived":false,"firstLLMTokenReceived":false,"firstSearchResultsMarker":{"eventTime":-1},"timestamp":' + str(int(time.time())) + ',"isBrowserExtension":false,"timeZone":"Asia/Makassar"},"visitor_id":"' + uidvisit + '","url":"/","referrer":"","language":"id","screen":"360x820","hostname":"www.perplexity.ai","device_info":{"hardwareConcurrency":8,"architecture":127,"colorDepth":24,"screenSize":"360x820"},"is_arc_browser":false}]', headers=cloudSolver(newSolver=session.cookies.get_dict())).text
            timeStopper = int(time.time())
            while True:
                r=session.get(f"{url1}{rand()}&sid={sid}", headers=cloudSolver(newSolver=session.cookies.get_dict())).text
                if '"status":"completed"' in r:
                    workerStatus = "Berhasil"
                    break
                if int(time.time()) - timeStopper >= 5:
                    workerStatus = "Timeout"
                    break
        except Exception as e:
            print(f"error: {e}")
            pass
        cloudSolver(newSolver=session.cookies.get_dict(), writeP=True)
        time.sleep(10)

def createSession():
    global session
    session = requests.Session()

def cloudSolver(newSolver=None, writeP=None):
    '''
    cookieFile = os.listdir()
    if "cookie.txt" not in cookieFile:
        baseSolver = {
            "pplx.visitor-id": "9592beea-3e19-4448-9b34-f357160cb170",
            "__stripe_mid": "e0505fa9-59d3-4420-b70b-9c2a4536887f07fdda",
            "__cflb": "02DiuDyvFMmK5p9jVbVnMNSKYZhUL9aGkroiSmxfMjbgQ",
            "cf_clearance": "8twTTzP6OXq072sXPT3Hb71hhYeWxRGwsXKGIdTP9hs-1725015570-1.2.1.1-F6E4Fsd6778vUSzhnH.qz.K2EUCKx52vVFnmDZ9iRsKGTOS.ZgTTnnaXQUJsj_5pYMDofWpDSEYIXY3bpInaETUNEg2.5p2hQF.AKVlgsE7oDbp5CpM_IsoYgycc89sc263L2hs6_9LiIjp4BEbkpsjYGGb.D.7RfDImFBZYb_Op4PMkmcEkHPoyAkzWhB_gfLZGIBf6JjK8p7gvUcJR9M4MYjonYSJI.2DJTQD57d.5Y3W3NEEnnxus0eTF5R0HjxmqxsNabZWXaJsqyvwFcXAzBxV84k2piNGwFg8bgm6vx0yTzwZ9ukDxRjWHuEIjmvB3KsYsHMyBNL3Zrxck4W5P9A_hFVj4ApeiBA4m3DwJ5aJRGEKzRhyzFW4080NwvKprH_eih2fucszfxXmi_Mg.eS.hh7txx.ds04QFW_tslayW7CeMvEMlw7D2aK4H",
            "AWSALB": "Ku6xMdPsjpYpHRTH2Kiic2EKXYIPKLvqSo4IOX1ONaCAEvw6vrorS0bxQVgsHN07fp9a2fca/4iV4mzbBnOaXZKFstkBlrhiOij7WHJvorc1y1kipOkGOxpQ9X9RD7lXhSOmCJxClErKpcKu2RdihS/r46FlGcOX+DMojXN6FM49xukgOMHiroKuT8972PZ5sGwdXubdZ8NJdms95CF7ZRq3pAXfloGM1UdJLbEp4n2tSVYw9BNAERQX+Z9ZokI=",
            "AWSALBCORS": "Ku6xMdPsjpYpHRTH2Kiic2EKXYIPKLvqSo4IOX1ONaCAEvw6vrorS0bxQVgsHN07fp9a2fca/4iV4mzbBnOaXZKFstkBlrhiOij7WHJvorc1y1kipOkGOxpQ9X9RD7lXhSOmCJxClErKpcKu2RdihS/r46FlGcOX+DMojXN6FM49xukgOMHiroKuT8972PZ5sGwdXubdZ8NJdms95CF7ZRq3pAXfloGM1UdJLbEp4n2tSVYw9BNAERQX+Z9ZokI=",
            "__cf_bm": "4MWt2UFFPFQGWlTxTTDpEtPV.XuJXE4nUxqxgdyw7CY-1725015587-1.0.1.1-.NFV3b2rGdosGJjSz2uYAU_6z6AAzQnJ6spW9nfhv0k3xSllaD9SxAu.h3NskfCDMBgWNKO8eUXNfhvDbalKCg",
        }
    else:
        baseSolver = eval(open("cookie.txt", "r").read())
    if newSolver:
        for key, value in newSolver.items():
            baseSolver[key] = value
    if writeP:
        open("cookie.txt", "w").write(str(baseSolver))
    '''
    headers = {
        'authority': 'www.perplexity.ai',
        'accept': '*/*',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-environment=dev,sentry-release=jsfkG4eiVywZFr7LerMQ0,sentry-public_key=bb45aa7ca2dc43b6a7b6518e7c91e13d,sentry-trace_id=a9e1685e73f44d85b3af45681ffdeea5,sentry-sample_rate=0,sentry-sampled=false',
#        'cookie': "; ".join(f"{key}={value}" for key, value in baseSolver.items()),
        'referer': 'https://www.perplexity.ai/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '4e9aac52c89944929a740bec2754666f-814ebfa878ba9f82-0',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    return headers

def rand(mode=0):
    if mode:
        return "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(5))
    return "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(2))

def perplexity(prompt):
    if not session:
        createSession()
    uidcontext = str(uuid.uuid4())
    uidfrontend = str(uuid.uuid4())
    uidvisit = str(uuid.uuid4())
#    uidvisit = re.search("pplx.visitor-id=(.*?);", cloudSolver()["cookie"]).group(1)
    url1 = f'https://www.perplexity.ai/socket.io/?EIO=4&transport=polling&t={rand(mode=1)}'
    r = session.get(f"{url1}{rand()}", headers=cloudSolver()).text
    sid = re.search("\"sid\":\"(.*?)\"", r).group(1)
    p = session.post(f"{url1}{rand()}&sid={sid}", data='40{"jwt":"anonymous-ask-user"}', headers=cloudSolver()).text
    p = session.post(f"{url1}{rand()}&sid={sid}", data='4214["perplexity_ask","' + prompt.replace("\n", ". ") + '",{"version":"2.9","source":"mweb","attachments":[],"language":"id","timezone":"Asia/Makassar","search_focus":"internet","frontend_uuid":"' + uidfrontend + '","mode":"concise","is_related_query":false,"visitor_id":"' + uidvisit + '","frontend_context_uuid":"' + uidcontext + '","prompt_source":"user","query_source":"home","is_incognito":false,"time_from_first_type":13200}]\u001e42["analytics_event",{"version":"2.9","source":"mweb","event_name":"submit query","event_data":{"queryStr":"' + prompt + '","queryParams":{"attachments":[],"language":"id","timezone":"Asia/Makassar","search_focus":"internet","frontend_uuid":"' + uidfrontend + '","mode":"concise","is_related_query":false,"visitor_id":"' + uidvisit + '","frontend_context_uuid":"' + uidcontext + '","prompt_source":"user","query_source":"home","is_incognito":false,"time_from_first_type":13200},"isFollowup":false,"submissionCount":1,"submissionType":"perplexity_ask","frontendUUID":"' + uidfrontend + '","submitTimestamp":' + str(int(time.time())) + ',"startFirstServerResponseMarker":{"eventTime":-1},"startLLMTokenMarker":{"eventTime":-1},"endStreamTimestamp":null,"finalizedTimestamp":null,"firstServerResponseReceived":false,"firstLLMTokenReceived":false,"firstSearchResultsMarker":{"eventTime":-1},"timestamp":' + str(int(time.time())) + ',"isBrowserExtension":false,"timeZone":"Asia/Makassar"},"visitor_id":"' + uidvisit + '","url":"/","referrer":"","language":"id","screen":"360x820","hostname":"www.perplexity.ai","device_info":{"hardwareConcurrency":8,"architecture":127,"colorDepth":24,"screenSize":"360x820"},"is_arc_browser":false}]', headers=cloudSolver()).text
    dataFinal = "Result tidak ditemukan"
    while True:
        r=session.get(f"{url1}{rand()}&sid={sid}", headers=cloudSolver()).text
        if '"status":"completed"' in r:
            res = eval("'''" + r + "'''")
            result = re.search("\"status\":\"completed\".*\"text\":\"\{\"answer\": \"(.*?)\", \"web_results\": \[.*?\], \"chunks\"", res)
            if result:
                dataFinal = str(eval("'''" + result.group(1) + "'''"))
            break
#    cloudSolver(newSolver=session.cookies.get_dict(), writeP=True)
    return dataFinal

@app.route("/api", methods=["GET"])
def freeApi():
    p=request.args.get("prompt")
    if not p or p.replace(" ", "") == "":
        return jsonify({"status": "error","message": "prompt parameter is required"})
    return jsonify({"status": "success","output": perplexity(p)})

'''
@app.route("/cookie_guard", methods=["GET"])
def cookieGuard():
    if not workerStatus:
        executor.submit(sessionUpdate)
    return str(workerStatus)
'''

@app.route("/<apapun>", methods=["GET"])
def handler(apapun):
    return jsonify({"status": "error","message": f"path /{apapun} tidak ada"})

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "error","message": "gunakan path /api"})
