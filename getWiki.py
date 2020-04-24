import wikipedia

searchTerm = "Android"
numberOfArticles = 6
randomArticleList = wikipedia.random(pages=numberOfArticles)


print(randomArticleList)


# print(wikipedia.search("Programming"))
# print(wikipedia.summary(searchTerm, sentences=3))


# print(wikipedia.page(searchTerm))

# print(wikipedia.page("Python").content)
