strings = ["python", "c", "c++", "Lua"]

def sort_strings_by_length(strings, ascending=True):
    return sorted(strings, key=len, reverse=not ascending)


class Word:
    def __init__(self, Name):
        self.Name = Name
        self.Size = len(Name)
    
    @staticmethod
    def create_map(array_words):
        answer_list = []
        for word in array_words:
            answer_list.append(Word(word))
        return answer_list

    @staticmethod
    def get_map(array_word_list):
        answer_list_name = []
        for word in array_word_list:
            answer_list_name.append(word.Name)
        return answer_list_name

def bubble_sort_with_positions_dict(strings):
    arr = Word.create_map(strings)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].Size > arr[j+1].Size:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Меняем объекты местами
    sorted_names = Word.get_map(arr)
    return sorted_names

print(bubble_sort_with_positions_dict(strings))
print(sort_strings_by_length(strings))
