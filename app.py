from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from enum import Enum
from typing import Optional, List
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import mysql.connector as mysql

# Initialization section
app = FastAPI()
load_dotenv()
llm = ChatGoogleGenerativeAI(
    model= 'gemini-3.5-flash',
    temperature= 0.7
)

# Connect the database
con = mysql.connect(
    host = os.getenv('DB_HOST'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME'),
    port = int(os.getenv('DB_PORT')),
    user = os.getenv('DB_USER') 
)
cur = con.cursor()

# Status of order (To validate the order status)
class OrderStatus(str, Enum):
    Pending = 'pending'
    In_Progress = 'in_progress'
    Completed = 'completed'

# Schema validation for response and request
class WorkOrder(BaseModel):
    id: int
    title: str
    detail: str
    priority: str
    order_status: str


# Create work order
@app.post('/work_orders')
def create_work_order(work_order:WorkOrder):
    cur.execute('INSERT INTO work_orders (id,title,detail,priority,order_status) VALUES (%s,%s,%s,%s,%s)',
    (work_order.id,work_order.title,work_order.detail,work_order.priority,work_order.order_status))
    con.commit()

    return work_order

# List all work orders
@app.get('/work_orders')
def get_all_orders():
    cur.execute('SELECT * FROM work_orders')
    all_orders = cur.fetchall()
    if not all_orders:
        raise HTTPException(status_code=404, detail='No orders found')

    return all_orders

# Get by ID
@app.get('/work_orders/{order_id}')
def get_a_order(order_id: int):
    cur.execute('SELECT * FROM work_orders where id = %s', (order_id,))
    order = cur.fetchone()
    if not order:
        raise HTTPException(status_code=404,detail='No order found')
    return order

# Update order status
@app.put('/work_orders/{order_id}')
def update_order(order_id: int, status: str):
    cur.execute('UPDATE work_orders SET order_status=%s WHERE id=%s', (status, order_id))
    con.commit()
    return {'message': 'Status updated successfully.'}

# Sammurize the work order description
@app.post('/work_orders/{order_id}/sammurize')
def sammury(order_id):
    reply = llm.invoke(f'You are a hepful assistant. Sammurize this work order for me: {order_id}')
    return reply.text