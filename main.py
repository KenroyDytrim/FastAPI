import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def FIO():
    return {"FIO": "Корней Дмитрий Владимирович"}

@app.get('/users')
async def Data():
    return {"number": "89039192952", "email": "korney1404@gmail.com"}

@app.get('/tools')
async def Tools():
    return "Владеет языками программирования: C++, C#, Python, R, JavaScript"

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)