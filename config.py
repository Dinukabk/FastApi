
from supabase_py import create_client,Client


url = "https://evgktdajwsznfupmtkrr.supabase.co"
key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYyNzA0Mjg4MCwiZXhwIjoxOTQyNjE4ODgwfQ.l00AjvwvT70rGUR8QRvdR7eNxA2xXp73H14S9ttcIT4"

supabase:Client = create_client(url,key)

