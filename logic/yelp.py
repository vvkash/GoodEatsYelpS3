import requests


location = input("Enter City or State Name: ")
search_url = "https://www.yelp.com/search/snippet?find_desc=Restaurants&find_loc=" + location + "&request_origin=user"
search_response = requests.get(search_url)
search_results = search_response.json()['searchPageProps']['mainContentComponentsListProps']

for result in search_results:
    if result['searchResultLayoutType'] == "iaResult":
        print(result['searchResultBusiness']['name'])
        print(result['searchResultBusiness']['reviewCount'], "Reviews")
        print(result['searchResultBusiness']['rating'],"/ 5", "Stars")
        print("https://www.yelp.com" + result['searchResultBusiness']['businessUrl'])
        print("--------")

