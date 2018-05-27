from collections import Counter

import math


class Tf_idf:
    def __init__(self, Data):
        self.data = Data
        self.calculate()
    def calculate(self):
        for data in self.data:
            print(data.component)
            countlist = []
            kinfe = []
            for text in data.text:
                for i in text:
                    if i.filterlast == False:
                        kinfe.append(i.kinfe)
            countlist.append(self.count_term(kinfe))
            for i, count in enumerate(countlist):
                filter = []
                # filter.append(kinfe[-1])
                # print("Top words in document" + str(int(i) + 1))
                scores = {word: self.tfidf(word, count, countlist) for word in count}
                print(scores)
                for key, value in count.items():
                    print(value)
                    if value == 1.0:
                        filter.append(key)
                # print(filter)
                for j in filter:
                    data.add_filter(j)
                sorted_words = sorted(scores.items(), key=lambda x: x[1])
                # for word, score in sorted_words[:]:
                #     print("Word: " + word+", TF-IDF: " + str(score))
    def count_term(self, text):
        count = Counter(text)
        print(count.most_common())
        return count

    def tf(self, word, count):
        return count[word] / sum(count.values())

    def n_containing(self, word, count_list):
        return sum(1 for count in count_list if word in count)

    def idf(self, word, count_list):
        return math.log(len(count_list)) / (1 + self.n_containing(word, count_list))

    def tfidf(self, word, count, count_list):
        return self.tf(word, count) #* self.idf(word, count_list)