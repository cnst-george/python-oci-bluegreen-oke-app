from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/")
def read_root():
    version="1.0"
    namespace = os.getenv('POD_NAMESPACE', default = 'ns-red')
    return {"Message": "with Love from OCI Devops - ISV Demo ","Version":version,"Namespace":namespace}
