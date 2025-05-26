## Token Auth
## DB : User, analytics

## 

from fastapi import FastAPI, Request, Response, HTTPException
from requestSchema import AnalyticsRequest, EventTypes

app = FastAPI()


@app.get('/ping')
def getStatus(request:Request, response:Response):
    return {"message": "pong"}


@app.post('/user/1/activity')
async def getAnalyticsData(data: AnalyticsRequest,response:Response):
    print(await data.json())
    """
    payload: 
    {
        "event_type": "pageview"
        "timestamp": "2025-05-15T10:12:00Z",
        "metadata": {
            "page": "/home",
            "browser": "Chrome"
            }
    }

    response: {"message": "activity recorded"}
    """
    analytics_request_body = await data.json()
    try:
        if 'event_type' not in analytics_request_body or (
            analytics_request_body['event_type'] not in ['pageview']
        ):
            return HTTPException(400, {"error": "invalid event_type  found in request" }) 
        return {"message": "activity recorded"}
    except Exception as msg:
        return HTTPException(500, {"error": "internal error" , "msg": str(msg)}) 


