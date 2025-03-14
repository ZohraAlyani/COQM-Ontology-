# COQM-Ontology
  
It is a modular ontology designed to formalize and structure quality management in business processes. Based on DOLCE (Descriptive Ontology for Linguistic and Cognitive Engineering), it enables the integration of key quality concepts and management standards directly into BPMN (Business Process Model and Notation).

This implementation covers the following steps to achieve our objective, which is the construction of the ontology. We follow the necessary stages:
1) Domain analysis
2)  Conceptualization
3) Implementation

--> Our ontology is composed of multiple ontological modules, covering key aspects such as knowledge, performance indicators, objectives, risks, and quality artefacts.
 
COQM was developed using the Protégé , an open source platform for creating and editing ontologies. Protégé supports multiple ontology languages, including RDF, OWL, and XML, and can be extended with plugins to extend its functionality.


Figure 1: ontology global view

In the following, the ontological modules include Process ,Risk, Objectives, Quality-Artefacts, Prformance Indicator and knowledge .


Figure 2: Ontological module for Quality Artefact
Figure 3: Ontological module for Performance Indicator

Figure 4: Ontological module for Knowledge
Figure 5:Ontological module for ObjectiveFigure 6: Ontological module for Process

Figure 7:Ontological module for Risk



I have applied some rules: 
* SPARQL query to list Class 
* SPARQL query to list individuals with their class
* SPARQL query to list Object Properties with their Domains and Ranges




I have implemented a Python script to load our ontology and retrieve the list of classes, subclasses, individuals, object properties, and execute SPARQL queries.
==> from owlready2 import * 
==> chemin_owl = r"C:\Users\hp\Desktop\CODE\COQM.owl" 
==> onto = get_ontology(chemin_owl).load()



==> FastAPI to create an API that returns classes and instances.
==> I have already created an API for our ontology{ Get Classes,Get Instances, Get Relations, Add Instances }
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs






