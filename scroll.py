from connect import *

# Search Query
max_document_per_search = 1000
es_query = {
    "size": max_document_per_search,
    "query": {
        "match_all": {}
    }
}

# es_query.update({"size": max_document_per_search })

if __name__ == "__main__":
    response = my_instance.search(index="kibana_sample_data_flights", body=es_query, scroll="3m")
    #get first 1000 documents using search query

    '''
        In above line three para are passed
            1.  index
            2.  query this is changed from (body) 
            3.  scroll duration for which scroll should be alive

            the output of search query will stored in response variable 
            -   number of documents found in search query can be found
                    len(response.get('hits,{}).get('hits))
            -   scroll id can be found as
                    response.get('_scroll_id')
            -   we need to use .get method insted of [] to avoid errors


            while condition:
                pass

            while len(response.get('hits',{}).get('hits')) == max_documents_per_search:
                response = my_instance.scroll(scroll_id=my_scroll_id, scroll="1m")
                print(f"found{len(response.get('hits',{}).get('hits'))} number of documents")

    '''

    # first we get 1000 hits/record here before while loop
    print(f"found before while{len(response.get('hits',{}).get('hits'))} number of documents")
    my_scroll_id = response.get('_scroll_id')

    #continue scrolling (searching) through es index until returned documents are not less than 1000
    while len(response.get('hits',{}).get('hits')) == max_document_per_search:
        response = my_instance.scroll(scroll_id=my_scroll_id, scroll="1m")
        print(f"found after while{len(response.get('hits',{}).get('hits'))} number of documents")
