from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    age: int
    size: int
    category: str
    budget : int
 
class Consultation(BaseModel):
    id: int
    user_id: int
    sneakers_id: int
    consult_url: str
    
class Details(BaseModel):
    size: int
    stock: int
    price: int
 
class Sneakers(BaseModel):
    id: int
    name: str
    details: List[Details]
    category:str

json_filename="sneakersconsult.json"

with open(json_filename,"r") as read_file:
    data = json.load(read_file)

app = FastAPI()

@app.get('/sneakers')
async def read_all_sneakers():
    return data['sneakers']

@app.get('/sneakers/{sneaker_id}')
async def read_sneaker(sneaker_id: int):
    for sneaker in data['sneakers']:
        print(sneaker)
        if sneaker['id'] == sneaker_id:
            return sneaker
    raise HTTPException(
        status_code=404, detail=f'sneaker not found'
    )
 
@app.get('/consult')
async def read_all_consultations():
    return data['consultation']

@app.get('/consult/{user_id}')
async def read_consult(user_id: int):
    for consult in data['consultation']:
        print(consult)
        if consult['user_id'] == user_id:
            return consult
    raise HTTPException(
        status_code=404, detail=f'user not found'
    )
 
@app.post('/sneakers')
async def add_sneakers(sneakers: Sneakers):
    sneakers_dict = sneakers.dict()
    sneakers_found = False
    for sneakers_item in data['sneakers']:
        if sneakers_item['id'] == sneakers_dict['id']:
            sneakers_found = True
            return "sneakers ID "+str(sneakers_dict['id'])+" exists."
    
    if not sneakers_found:
        data['sneakers'].append(sneakers_dict)
        with open(json_filename,"w") as write_file:
            json.dump(data, write_file, indent=4)

        return sneakers_dict
    raise HTTPException(
        status_code=404, detail=f'sneaker not found'
    )

@app.get('/user')
async def read_all_users():
    return data['user']

@app.get('/user/{user_id}')
async def read_user(user_id: int):
    for user in data['user']:
        print(user)
        if user['id'] == user_id:
            return user
    raise HTTPException(
        status_code=404, detail=f'user not found'
    )

@app.post('/user')
async def add_user(user: User):
    user_dict = user.dict()
    user_found = False
    for user_item in data['user']:
        if user_item['id'] == user_dict['id']:
            user_found = True
            return "User ID "+str(user_dict['id'])+" exists."
    
    if not user_found:
        data['user'].append(user_dict)
        with open(json_filename,"w") as write_file:
            json.dump(data, write_file, indent=4)

        return user_dict

    raise HTTPException(
        status_code=404, detail=f'user not found'
    )
    
@app.put('/user')
async def update_user(user: User):
	user_dict = user.dict()
	user_found = False
	for user_idx, user_item in enumerate(data['user']):
		if user_item['id'] == user_dict['id']:
			user_found = True
			data['user'][user_idx]=user_dict
			
			with open(json_filename,"w") as write_file:
				json.dump(data, write_file, indent=4)
			return "updated"
	
	if not user_found:
		return "User ID not found."
	raise HTTPException(
		status_code=404, detail=f'user not found'
	)  
 
 
@app.put('/sneakers')
async def update_sneaker(sneaker: Sneakers):
	sneaker_dict = sneaker.dict()
	sneaker_found = False
	for sneaker_idx, sneaker_item in enumerate(data['sneakers']):
		if sneaker_item['id'] == sneaker_dict['id']:
			sneaker_found = True
			data['sneakers'][sneaker_idx]=sneaker_dict
			
			with open(json_filename,"w") as write_file:
				json.dump(data, write_file, indent=4)
			return "updated"
	
	if not sneaker_found:
		return "sneaker ID not found."
	raise HTTPException(
		status_code=404, detail=f'sneaker not found'
	)    
    
 
@app.post('/consult/{user_id}')
async def do_consult(user_id : int):
    consultSneakers = []
    found = False
    for user in data['user']:
        if user['id'] == user_id:
            found_user = user
            found = True

    if(not found):
        raise HTTPException(
            status_code=404, detail=f'user not found'
        )
    
    for sneaker in data['sneakers']:
        if(sneaker['category'] == found_user['category'] and sneaker['details']):
            for detail in sneaker['details']:
                if(detail['size'] == found_user['size'] and detail['price'] <= found_user['budget']):
                    consultSneakers.append(sneaker['id'])
                    break;
    
    if not consultSneakers:
        consultData = {
        "user_id" : found_user['id'],
        "sneaker_id" : '',
        "consult_notes" : "Tidak ada sneakers yang cocok dari segi size, category, ataupun budget"
    }
    else:
        consultData = {
            "user_id" : found_user['id'],
            "sneaker_id" : consultSneakers[0],
            "consult_notes" : "http://dummyimage.com/1920x1080"
        }
    
    data['consultation'].append(consultData)
    with open(json_filename,"w") as write_file:
        json.dump(data, write_file, indent=4)
    
    return consultData
    raise HTTPException(
        status_code=404, detail=f'sneaker not found'
    )