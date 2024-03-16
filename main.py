from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import  psycopg2  

app = FastAPI()


@app.get('/')
async def home_page():
    return  "Created with ❤️ By Team Neoteric"



@app.post("/insert-into-db")
async def insert_into_db(
    user_name: str = Form(...),
    user_address: str = Form(...),
    user_email: str = Form(...),
    contact_number: str = Form(...),
    user_country: str = Form(...)
):
    # Now you can do whatever you need to do with this data, like inserting it into a database
    # For example, printing it for demonstration purposes:
    print("Name:", user_name)
    print("Address:", user_address)
    print("Email:", user_email)
    print("Contact Number:", contact_number)
    print("Country:", user_country)
    try:
        conn = psycopg2.connect(
            "postgres://pmiwcsmy:UiG8q1pOAKnRVb85ed3GCGn5W3qaCvIx@flora.db.elephantsql.com/pmiwcsmy",
            
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO users (user_name, user_address, user_email, contact_number, user_country) VALUES (%s, %s, %s, %s, %s)", (user_name, user_address, user_email, contact_number, user_country))
        conn.commit()
        conn.close()
        return {"message": "Data received successfully."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
    