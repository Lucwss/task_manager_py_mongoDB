from .server.routes.task_routes import router as TaskRoutes
from .server.routes.user_routes import router as UserRoutes
from .server.routes.auth.auth_route import router as AuthRoutes
from .server.routes.services.services_route import router as ServicesRoutes
from .server.helpers.auth.methods import *
from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(TaskRoutes, prefix='/task', tags=['Task Routes'], dependencies=[Depends(get_current_active_user)])
app.include_router(UserRoutes, prefix='/user', tags=['User Routes'], dependencies=[Depends(get_current_active_user)])
app.include_router(AuthRoutes, prefix='/auth', tags=['Auth Routes'])
app.include_router(ServicesRoutes, prefix='/service', tags=['Services Routes'])


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


''' Current main root route '''


@app.get("/", tags=["Root"])
async def read_root():
    return {'message': 'welcome to my personal project'}

if __name__ == '__main__':
    uvicorn.run('api.application:app', reload=True)

