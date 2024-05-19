# recommend/recommendation_engine.py
import json
from pybloom_live import BloomFilter
from os.path import join
from django.conf import settings

# Load the Association Rule Model
with open(join(settings.BASE_DIR,"data/frequent_itemsets.json"), "r") as f:
    frequent_itemsets = json.load(f)

with open(join(settings.BASE_DIR,"data/association_rules.json"), "r") as f:
    association_rules = json.load(f)

# Load the Collaborative Filtering Model
with open(join(settings.BASE_DIR,"data/user_recommendations.json"), "r") as f:
    user_recommendations = json.load(f)


with open(join(settings.BASE_DIR,"data/tracks.json"), "rb") as f:
    tracks = json.load(f)


# flatten the frequent itemsets
frequent_itemsets_flat = []
for itemset in frequent_itemsets:
    frequent_itemsets_flat.append(itemset['items'])


def get_association_rule_recommendations(user_id):
    # Implement logic to get recommendations based on association rules
    recommendations = []
    bloom_filter = BloomFilter(capacity=100000, error_rate=0.001)
    for rule in association_rules:
        # Example logic to get recommendations
        if rule['antecedent'] in frequent_itemsets_flat:
            recommendations.extend(rule['consequent'])
    
    # Use Bloom Filter to filter out already recommended items
    filtered_recommendations = []
    
    # Add new recommendations to the Bloom Filter
    for track in recommendations:
        if track not in bloom_filter:
            filtered_recommendations.append(track)
            bloom_filter.add(track)
            
    
    return filtered_recommendations

def get_collaborative_filtering_recommendations(user_id):
     
    recommendations = user_recommendations.get(str(user_id), [])
    
    # Use Bloom Filter to filter out already recommended items

    bloom_filter = BloomFilter(capacity=100000, error_rate=0.001)

    filtered_recommendations = []
    
    # Add new recommendations to the Bloom Filter
    for track in recommendations:
        track_name = tracks['trackname'].get(str(track)+'.0', "Unknown")
        if track_name not in bloom_filter:
            
            filtered_recommendations.append(track_name)
            bloom_filter.add(track_name)
    
    return filtered_recommendations
