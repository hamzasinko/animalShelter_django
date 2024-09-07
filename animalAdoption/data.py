from models import chien, chat, oiseau
data = {
    "chi": [
        {
            "nom" : "Max",
            "age" : 2,
            "statut_vaccinal" : True,
            "sterilisation" : True
        },
        {
            "nom" : "Luna",
            "age" : 5,
            "statut_vaccinal" : True,
            "sterilisation" : False
        },
        {
            "nom" : "Cooper",
            "age" : 3,
            "statut_vaccinal" : True,
            "sterilisation" : True
        },
        {
            "nom" : "Bella",
            "age" : 7,
            "statut_vaccinal" : True,
            "sterilisation" : False
        }
    ],
    "cha": [
        {
            "nom" : "Oliver",
            "age" : 4,
            "statut_vaccinal" : True,
            "sterilisation" : True
        },
        {
            "nom" : "Milo",
            "age" : 6,
            "statut_vaccinal" : True,
            "sterilisation" : False
        },
        {
            "nom" : "Simba",
            "age" : 2,
            "statut_vaccinal" : False,
            "sterilisation" : False
        },
        {
            "nom" : "Daisy",
            "age" : 2,
            "statut_vaccinal" : True,
            "sterilisation" : False
        }
    ],
    "oi": [
        {
            "nom" : "Kiwi",
            "age" : 1,
            "statut_vaccinal" : True,
            "sterilisation" : False
        },
        {
            "nom" : "Peaches",
            "age" : 2,
            "statut_vaccinal" : True,
            "sterilisation" : False
        },
        {
            "nom" : "Sunny",
            "age" : 3,
            "statut_vaccinal" : True,
            "sterilisation" : False
        },
        {
            "nom" : "Coco",
            "age" : 1,
            "statut_vaccinal" : True,
            "sterilisation" : False
        }
    ]
}
for a in data["cha"]:
     db1 = chat(nom=a["nom"],age=a["age"],statut_vaccinal=a["statut_vaccinal"],sterilisation=a["sterilisation"])
     db1.save()
for b in data["oi"]:
     db2 = oiseau(nom=b["nom"],age=b["age"],statut_vaccinal=b["statut_vaccinal"],sterilisation=b["sterilisation"])
     db2.save()
for c in data["chi"]:
     db3 = chien(nom=c["nom"],age=c["age"],statut_vaccinal=c["statut_vaccinal"],sterilisation=c["sterilisation"])
     db3.save()