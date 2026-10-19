
class TokensHandling:
    def MostFrequentPair(self,tokens):
        count = 0
        freq =0
        freq_pair = None

        for i in range(len(tokens)):
            count = 0

            for j in range(len(tokens)):
                if tokens[i] == tokens[j]:
                    count = count +1
            if count > freq:
                freq = count
                freq_pair = tokens[i]


        return freq, freq_pair



tokens = [22, 33, 44, 44, 66, 777, 777, 22, 99, 33, 55, 10, 22, 777, 777]
tokenHandling = TokensHandling()
most_frequent_Pair, their_frequency = tokenHandling.MostFrequentPair(tokens)
print("Most frequent pair is: ", most_frequent_Pair, "Their frequency: ", their_frequency)









