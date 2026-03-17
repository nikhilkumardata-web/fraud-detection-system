import time

async def timing_middleware(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"Request took {duration:.4f} seconds")
    return response
