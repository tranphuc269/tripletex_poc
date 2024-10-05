base_url = 'https://api.tripletex.io/v2'
consumer_token = 'eyJ0b2tlbklkIjozNTMxLCJ0b2tlbiI6InRlc3QtNDhkNzdjYzItNjc5ZS00MTc0LWI4OTAtMWNmMWQ4YWNiZmVlIn0='
employee_token = 'eyJ0b2tlbklkIjo1NzE2LCJ0b2tlbiI6InRlc3QtNmE2OWZmMWItOWQyYi00NmNjLWI3YWUtNTlhOGUwZmJlNjM0In0='

expiration_date = '2026-01-01'


class Config:
    def __init__(self):
        self.base_url = base_url
        self.consumer_token = consumer_token
        self.employee_token = employee_token
        self.expiration_date = expiration_date
