from fastapi import FastAPI
from owlready2 import *

# Charger l'ontologie (remplace par ton chemin de fichier OWL)
onto = get_ontology(r"C:\Users\hp\Desktop\CODE\COQM.owl").load()

# Initialiser l’API
app = FastAPI(title="COQM : A core Ontology of Quality Management ", description="API pour interroger une ontologie OWL", version="1.0")

# 📌 1️⃣ Endpoint : Obtenir toutes les classes de l'ontologie
@app.get("/classes")
def get_classes():
    classes = [cls.name for cls in onto.classes()]
    return {"classes": classes}

# 📌 2️⃣ Endpoint : Obtenir toutes les instances d'une classe donnée
@app.get("/instances/{class_name}")
def get_instances(class_name: str):
    cls = onto.search_one(name=class_name)
    if cls:
        instances = [inst.name for inst in cls.instances()]
        return {"class": class_name, "instances": instances}
    return {"error": "Classe non trouvée"}




# 📌 3️⃣ Endpoint : Obtenir les relations d’une instance
@app.get("/relations/{instance_name}")
def get_relations(instance_name: str):
    inst = onto.search_one(name=instance_name)
    if not inst:
        return {"error": "Instance non trouvée"}
    
    relations = {}
    for prop in onto.object_properties():
        related_instances = getattr(inst, prop.name, [])
        if related_instances:
            relations[prop.name] = [r.name for r in related_instances]

    return {"instance": instance_name, "relations": relations}

# 📌 4️⃣ Endpoint : Ajouter une nouvelle instance à une classe
@app.post("/add_instance/{class_name}/{instance_name}")
def add_instance(class_name: str, instance_name: str):
    cls = onto.search_one(name=class_name)
    if not cls:
        return {"error": "Classe non trouvée"}
    
    new_instance = cls(instance_name)
    onto.save()  # Sauvegarder l’ontologie
    return {"message": f"Instance '{instance_name}' ajoutée à la classe '{class_name}'"}


@app.get("/instances/{class_name}")
def get_instances(class_name: str):
    cls = onto.search_one(iri="*" + class_name)  # Rechercher par IRI aussi
    if cls:
        instances = list(cls.instances())
        print(f"Instances de {class_name} : {instances}")  # Debugging
        return {"class": class_name, "instances": [inst.name for inst in instances]}
    return {"error": "Classe non trouvée ou sans instances"}
    
    

# Lancer le serveur FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "🚀 API FastAPI fonctionne parfaitement !"}

    

# Lancer le serveur
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    from fastapi.responses import FileResponse

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")