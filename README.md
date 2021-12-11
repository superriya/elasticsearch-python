# elasticsearch-with-python
-  git status
-  git add file name or git add .
-  git commit "first-commit"
-  git push

### Connected python with Elasticsearch and work on multiple queries on Index

### Connection between python and elasticsearch
    my_instance = Elasticsearch(es_host,http_auth=(es_user, es_password),use_ssl=True, verify_certs=False)

    if not my_instance:
        print("Connection Error")
    else:
        print("Connection Successful!")

### Queries
-   add documents
        PUT index_name/_doc
-   search documents
        GET index_name/_search

# Scroll API
-   By default _search query can fetch 1000 number of documents data
-   But with the help of Scroll API we found in search query more than 1000's of documents data 
    1.  need to define index_name, query, scroll_time
        - syntax:
            <!-- -   got response -->
                response = my_instance.search(index="kibana_sample_data_flights", body=es_query, scroll="3m")
            
    2.  get scroll id and result
        -   syntax:
            <!-- -  first we get 1000 hits/record here before while loop -->
                print(f"found before while{len(response.get('hits',{}).get('hits'))} number of documents")
                my_scroll_id = response.get('_scroll_id')

    3.  we get all documents data with the help of while loop  
        -   syntax:
            <!-- -   while loop -->
                while len(response.get('hits',{}).get('hits')) == max_document_per_search:
                    response = my_instance.scroll(scroll_id=my_scroll_id, scroll="1m")
                    print(f"found after while{len(response.get('hits',{}).get('hits'))} number of documents")