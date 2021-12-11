# elasticsearch-with-python
-  git status
-  git add file name or git add .
-  git commit "first-commit"
-  git push

### connected python with elasticsearch and work on multiple queries like add documents, search documents for index

# Scroll API
-   By default _search query can fetch 1000 number of documents data
-   But with the help of Scroll API we found in search query more than 1000's of documents data 
    1.  need to define index_name, query, scroll_time
        - syntax:
            -   response = my_instance.search(index="kibana_sample_data_flights", body=es_query, scroll="3m")
            
    2.  get scroll id and result
        -   syntax:
            <!-- -  first we get 1000 hits/record here before while loop -->
                print(f"found before while{len(response.get('hits',{}).get('hits'))} number of documents")
                my_scroll_id = response.get('_scroll_id')

    3.  we get all documents data with the help of while loop  
        -   syntax:
            -   while len(response.get('hits',{}).get('hits')) == max_document_per_search:
                    response = my_instance.scroll(scroll_id=my_scroll_id, scroll="1m")
                    print(f"found after while{len(response.get('hits',{}).get('hits'))} number of documents")