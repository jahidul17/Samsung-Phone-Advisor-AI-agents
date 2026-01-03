from langchain.tools import tool
from database import SessionLocal
from sqlalchemy import text

@tool
def fetch_phone_specs(phone_name: str):
    """
    Fetches the technical specifications of a Samsung phone from the database.
    Use this tool when you need to know details about display, camera, RAM, 
    battery, or price of a specific Samsung model.
    """
    
    db = SessionLocal()
    try:
    
        query = text("""
            SELECT model_name, display, camera, ram, storage, battery, price 
            FROM samsung_phones 
            WHERE model_name ILIKE :name
        """)
        
        result = db.execute(query, {"name": f"%{phone_name}%"}).fetchone()
        
        if result:
            return {
                "Model": result[0],
                "Display": result[1],
                "Camera": result[2],
                "RAM": result[3],
                "Storage": result[4],
                "Battery": result[5],
                "Price": result[6]
            }
        
        return f"Sorry, no information was found for the model '{phone_name}' in the database."
        
    except Exception as e:
        return f"Database Error: {str(e)}"
    finally:
        db.close()