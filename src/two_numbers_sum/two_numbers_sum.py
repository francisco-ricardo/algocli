

def two_numbers_sum(array, targetSum):

    def tuples_generator(array):
        pair_heads_index = [x for x in range(0, (len(array) - 1))]
        pair_tails_index = [x for x in range(1, len(array))]

        for i in pair_heads_index:
            for j in pair_tails_index:
                if (j <= i):
                    continue
                yield(array[i], array[j],)


    def pair_sum():
        pass            


    array_pairs = [x for x in tuples_generator(array)]
    print(array_pairs)
