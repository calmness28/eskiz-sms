import aiohttp
import asyncio


async def send_sms(mobile_phone: str, message: str):
    url = "https://notify.eskiz.uz/api/message/sms/send"
    headers = {
        "Authorization": "Bearer <token>"  # notify.eskiz.uz/api/auth/login real token
    }
    payload = {
        "mobile_phone": mobile_phone,  # sms junatitmoqchi bugan telefon raqamiz
        "message": message,  # SMS
        "sender": "eskiz",  # nickname (default=4546)
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as response:
                if response.status == 200:
                    print("SMS yuborildi!")
                else:
                    response_data = await response.json()
                    print(f"Error: {response.status}, {response_data}")
    except Exception as e:
        print(f"Error: {e}")


async def main():
    mobile_phone = "998901234567"
    message = "Bu Eskiz dan test"
    await send_sms(mobile_phone, message)

if __name__ == "__main__":
    asyncio.run(main())
