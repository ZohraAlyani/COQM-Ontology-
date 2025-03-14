# COQM-Ontology
  
It is a modular ontology designed to formalize and structure quality management in business processes. Based on DOLCE (Descriptive Ontology for Linguistic and Cognitive Engineering), it enables the integration of key quality concepts and management standards directly into BPMN (Business Process Model and Notation).

This implementation covers the following steps to achieve our objective, which is the construction of the ontology. We follow the necessary stages:
1)	Domain analysis
2)	 Conceptualization
3)	Implementation

 Our ontology is composed of multiple ontological modules, covering key aspects such as knowledge, performance indicators, objectives, risks, and quality artefacts.
 
COQM was developed using the Protégé , an open source platform for creating and editing ontologies. Protégé supports multiple ontology languages, including RDF, OWL, and XML, and can be extended with plugins to extend its functionality.
![image](https://github.com/user-attachments/assets/c657e0cc-2141-4604-9e67-b6045d0e7d07)

 
Figure 1: ontology global view

In the following, the ontological modules include Process ,Risk, Objectives, Quality-Artefacts, Prformance Indicator and knowledge .

 ![image](https://github.com/user-attachments/assets/e22d0ab8-ca8a-46f7-894d-67e8c8de4af1)

Figure 2: Ontological module for Quality Artefact 
![image](https://github.com/user-attachments/assets/a6063719-f34e-4886-a88b-e913012e93f6)

Figure 3: Ontological module for Performance Indicator
 ![image](https://github.com/user-attachments/assets/14a6af4b-3970-4e8b-8a02-f54296373c58)

Figure 4: Ontological module for Knowledge
![image](https://github.com/user-attachments/assets/595ba60f-10ae-44d6-bc4a-902f6426651c)

 Figure 5:Ontological module for Objective 
 ![image](https://github.com/user-attachments/assets/584eec95-b06e-4872-960b-524736d6fcf2)


 Figure 6: Ontological module for Process
 ![image](https://github.com/user-attachments/assets/f5aa3309-8f63-442f-acde-6ebd497975bf)

Figure 7:Ontological module for Risk



I have applied some rules: 
	SPARQL query to list Class 
	SPARQL query to list individuals with their class
	SPARQL query to list Object Properties with their Domains and Ranges
 
 ![image](https://github.com/user-attachments/assets/ee11cecc-f034-4d12-baac-b4aaa6ccf66a)
 ![image](https://github.com/user-attachments/assets/2507db22-2e56-47b0-8c5e-2a365280bb14)
 ![image](https://github.com/user-attachments/assets/b8e309b3-290c-44b8-a82b-92854d214f91)



 

I have implemented a Python script to load our ontology and retrieve the list of classes, subclasses, individuals, object properties, and execute SPARQL queries.
	from owlready2 import * 
	chemin_owl = r"C:\Users\hp\Desktop\CODE\COQM.owl" 
	onto = get_ontology(chemin_owl).load()



	FastAPI to create an API that returns classes and instances.
	I have already created an API for our ontology{ Get Classes,Get Instances, Get Relations, Add Instances }
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs

 ![image](https://github.com/user-attachments/assets/cf7b24ce-0ed1-4332-af95-581c0e08005b)
 ![image](https://github.com/user-attachments/assets/557dda5b-a3b1-4392-8128-4d49451200bb)
 ![image](https://github.com/user-attachments/assets/f46a44b2-17f9-4a35-915d-ce56ef1a2cfe)



 



