# from fastapi.testclient import TestClient
# from app.main import app
# import json

# client = TestClient(app)

# def test_post_demande():
#     response = client.post(
#         "/demande",
#         json={
#             "destinataire": "TESTmathieu993test@hotmail.com",
#             "expediteur": "TESTmathieu993test@hotmail.com",
#             "password": "TEST1234Majuscule",
#             "sujet": "Un super sujet test",
#             "message": "Pour un super message TEST une minute après",
#             "mois": 3,
#             "jour": 24,
#             "heure": 14,
#             "minutes": 41,
#             "est_envoye": False
#         }
#     )
#     print(response.json())
