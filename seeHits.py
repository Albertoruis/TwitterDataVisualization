from database import DAO

dao = DAO()

data = dao.getAllHits()

for item in data:
    print item

