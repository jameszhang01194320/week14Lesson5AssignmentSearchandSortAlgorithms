from flask import Flask, request

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

# Bubble Sort Algorithm Implementation

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# Implement the binary search algorithm 

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Task 1: 
# Implement the binary search algorithm for searching videos by title.

sorted_video_titles = bubble_sort(video_titles)


# Task 2:
# Develop a REST API endpoint using Flask that allows users to search for videos 
# by their titles using the binary search developed in Task 1. 
# This API should accept a search query via query parameter, POST request, 
# or dynamic route, as input and return the matching videos, if any.

@app.route('/search', methods=['POST'])
def search_videos_post():
    data = request.json
    query = data.get('title', None)
    if query:
        index = binary_search(sorted_video_titles, query)
        if index != -1:
            return jsonify({"title": sorted_video_titles[index]}), 200
        else:
            return jsonify({"error": "Video not found"}), 404
    return jsonify({"error": "No search query provided"}), 400

@app.route('/search/<string:title>', methods=['GET'])
def search_videos_dynamic(title):
    index = binary_search(sorted_video_titles, title)
    if index != -1:
        return jsonify({"title": sorted_video_titles[index]}), 200
    else:
        return jsonify({"error": "Video not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)