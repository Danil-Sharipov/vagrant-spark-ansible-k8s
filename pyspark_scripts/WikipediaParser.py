import requests
from bs4 import BeautifulSoup
from pyspark.sql import SparkSession
from pyspark.sql import Row

def get_wikipedia_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return None

def parse_wikipedia_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extracting section titles from the Wikipedia page
    section_titles = [section.text.strip() for section in soup.find_all('span', {'class': 'mw-headline'})]
    
    return section_titles

def main():
    wikipedia_url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    
    html_content = get_wikipedia_page_content(wikipedia_url)
    
    if html_content:
        parsed_data = parse_wikipedia_page(html_content)
        
        # Check if parsed_data is a list before converting to RDD
        if isinstance(parsed_data, list):
            spark = SparkSession.builder.appName("WikipediaParser").master("spark://127.0.0.1:7077/").getOrCreate()
            
            # Create RDD and transform data for PySpark DataFrame
            rdd = spark.sparkContext.parallelize(parsed_data)
            df = rdd.map(lambda x: Row(data=x)).toDF()

            df.show(10, truncate=False)

            spark.stop()
        else:
            print("Parsing did not return a list of data.")

if __name__ == "__main__":
    main()
