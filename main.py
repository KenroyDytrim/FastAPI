import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
async def FIO():
    return {"FIO": "Корней Дмитрий Владимирович"}

@app.get('/users')
async def Data():
    return {"number": "89039192952", "email": "korney1404@gmail.com"}

@app.get('/tools', response_class = HTMLResponse)
async def Tools():
    return "Владею языками программирования: C++, C#, Python, R, JavaScript. <br /> Знаком со следующими средами разработки: Visual Studio и Jupyter Notebook"

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)