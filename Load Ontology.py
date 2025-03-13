from owlready2 import * 
chemin_owl = r"C:\Users\hp\Desktop\CODE\COQM.owl" 
onto = get_ontology(chemin_owl).load()
onto.classes() 
print(f"✅ Ontologie chargée : {onto.base_iri if onto.base_iri else 'Non chargée'}")

# Vérifier s'il y a des classes
classes = list(onto.classes())
print(f"📌 Nombre de classes trouvées : {len(classes)}")

# Afficher les classes détectées
for cls in classes:
    print(f"🔹 {cls.name}")
   # Afficher toutes les instances (individus)
print("📌 Liste des instances dans l'ontologie :")
for instance in onto.individuals():
    print(f"🔹 {instance.name} - Classe: {instance.is_a}")
    # Afficher toutes les propriétés d'objet
print("📌 Liste des Object Properties dans l'ontologie :")
for prop in onto.object_properties():
    print(f"🔹 {prop.name}")
    print("\n📌 Détails des Object Properties :")
for prop in onto.object_properties():
    print(f"\n🔹 Propriété : {prop.name}")
    print("\n📌 Relations entre Instances via Object Properties :")
for prop in onto.object_properties():
    for instance in onto.individuals():
        valeurs = getattr(instance, prop.name, [])
        if valeurs:
            print(f"🔹 {instance.name} --({prop.name})--> {[v.name for v in valeurs]}")
