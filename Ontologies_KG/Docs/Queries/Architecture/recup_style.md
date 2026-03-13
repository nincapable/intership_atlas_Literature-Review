## REQUÊTE PIVOT : FILTRAGE ARCHITECTURAL

Description : Cette requête permet de récupérer les bâtiments appartenant à une famille de style donnée (ex: médiéval) même s'ils sont typés avec une sous-variante très précise (ex: gothique flamboyant).  
Argument : Remplacer <??style_cible> par l'URI de la classe souhaitée. (ex: fe:StyleMedieval ou fe:StyleGothique)

Template de Requête : 
```
    PREFIX fe:   <http://example.org/fire_and_evacuation#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX crm:  <http://www.cidoc-crm.org/cidoc-crm/>

    SELECT ?building ?nomStyle ?risque ?lienWiki
    WHERE {
    # 1. On cherche le type précis du bâtiment
    ?building a ?typePrecis .
    
    # 2. On remonte la hiérarchie jusqu'à l'argument cible
    ?typePrecis rdfs:subClassOf* ??style_cible .
    
    # 3. Extraction des métadonnées du thésaurus
    ?typePrecis rdfs:label ?nomStyle .
    ?typePrecis crm:P3_has_note ?risque .
    
    OPTIONAL { 
        ?typePrecis <http://xmlns.com/foaf/0.1/isPrimaryTopicOf> ?lienWiki 
    }
    
    FILTER(LANG(?nomStyle) = "fr")
}
```