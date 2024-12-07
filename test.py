from models import Users

print(Users.insert(tg_id=1232, first_name="Oleg").execute())
