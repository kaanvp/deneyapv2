import os
import uuid
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET", "product-images")

supabase: Client = None

if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

async def upload_file_to_supabase(file_data, filename, content_type):
    if not supabase:
        return None
    
    # Ensure bucket exists (optional, usually created manually)
    # try:
    #     supabase.storage.create_bucket(SUPABASE_BUCKET)
    # except:
    #     pass

    path = f"uploads/{uuid.uuid4()}_{filename}"
    
    # Upload to Supabase Storage
    response = supabase.storage.from_(SUPABASE_BUCKET).upload(
        path=path,
        file=file_data,
        file_options={"content-type": content_type}
    )
    
    if hasattr(response, 'error') and response.error:
        raise Exception(f"Supabase upload error: {response.error}")
        
    # Get Public URL
    url_response = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(path)
    return url_response
