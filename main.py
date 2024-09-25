from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from constants import SERVER_URL, PORT, ENV
from apps.calculator.route import router as calculator_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield  # This yields control to the lifespan context
    
# Initialize the FastAPI app with a custom lifespan
app = FastAPI(lifespan=lifespan)

# Adding CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Register a health check route
@app.get("/")
async def health():
    return {"message": "server is running"}


app.include_router(calculator_router, prefix='/calculate', tags=['calculate'])

# Running the app with uvicorn
if __name__ == "__main__":
    uvicorn.run(
        "main:app",          # The "module_name:app_instance" format for uvicorn
        host=SERVER_URL,               # Host URL (localhost in your case)
        port=int(PORT),                # Port must be an integer
        reload=(ENV == 'dev')          # Enable live-reload only in development mode
    )

