# REQUÊTE : Historique Temporel du Bâtiment

Description : Cette requête permet de récupérer les bornes chronologiques des événements majeurs de la vie d'un bâtiment (Construction, Destruction, Rénovation).  
Argument : Remplacer <URI_DU_BATIMENT> par l'URI réelle du bâtiment (ex: fe:CathedraleAmiens).  

Template de Requête :
```
    PREFIX fe: <http://example.org/fire_and_evacuation#>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?label ?constrStart ?constrEnd ?destruction ?renovStart ?renovEnd
    WHERE {
        # On cible le bâtiment spécifique
        BIND(<URI_DU_BATIMENT> AS ?building)
        
        ?building a fe:Building ;
                rdfs:label ?label .

        # 1. Événement de Construction (Souvent obligatoire pour le calcul de risque)
        OPTIONAL {
            ?building fe:hasConstructionEvent/crm:P4_has_time-span ?tsC .
            ?tsC crm:P82a_begin_of_the_begin ?constrStart .
            ?tsC crm:P82b_end_of_the_end ?constrEnd .
        }

        # 2. Événement de Destruction
        OPTIONAL {
            ?building fe:hasDestructionEvent/crm:P4_has_time-span ?tsD .
            ?tsD crm:P82a_begin_of_the_begin ?destruction .
        }

        # 3. Événements de Rénovation (Il peut y en avoir plusieurs)
        OPTIONAL {
            ?building fe:hasRenovationEvent/crm:P4_has_time-span ?tsR .
            ?tsR crm:P82a_begin_of_the_begin ?renovStart .
            ?tsR crm:P82b_end_of_the_end ?renovEnd .
        }
        
        FILTER(LANG(?label) = "fr")
    }
```