import asyncio
import requests

async def main():
    loop = asyncio.get_event_loop()
    future1 = loop.run_in_executor(None, requests.get, 'http://127.0.0.1:5000/sampleapi/printcust?mock_user_id=24') #GET Request 1
    future2 = loop.run_in_executor(None, requests.get, 'http://127.0.0.1:5000/sampleapi/printcust?mock_user_id=144') #GET Request 2
    future3 = loop.run_in_executor(None, requests.get, 'http://127.0.0.1:5000/sampleapi/printcust?mock_user_id=33')
    response1 = await future1
    response2 = await future2
    response3 = await future3
    print(response1.text)
    print(response2.text)
    print(response3.text)

#while True:
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
