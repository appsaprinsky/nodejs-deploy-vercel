import json
import requests


if __name__ == '__main__':


####Register

    # URL = "http://localhost:4001/register"
    # params = {
    #     "first_name": "niki4",    
    #     "last_name": "miki4",
    #     "email": "niki4@gmail.com",    
    #     "password": "NukeNuke"   


    # }
    
    
    # resp = requests.post(URL, json=params)
    # print(resp.text)



####Login
    URL = "http://localhost:4001/login"
    params = {
        "email": "niki4@gmail.com",    
        "password": "NukeNuke"   
    }
    
    
    resp = requests.post(URL, json=params)
    print(resp.text)


####Welcome
    # URL = "http://localhost:4001/welcome"

    # # params = {
    # #     "email": "niki@gmail.com",    
    # #     "password": "NukeNuke"           
    # # }
    # headers = {
    #     "x-access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjIzODZlNDJlMGQzMmQzNzBhZTg1ZjNkIiwiZW1haWwiOiJuaWtpNEBnbWFpbC5jb20iLCJpYXQiOjE2NDc4NjU1NjcsImV4cCI6MTY0Nzg3Mjc2N30.J5_E8SmituarH63ag9J84px4w9SHsZN2ULZlkIcC-y0"  
    # }
    
    
    # resp = requests.post(URL, headers=headers)
    # print(resp.text)
    # print(resp.status_code)




