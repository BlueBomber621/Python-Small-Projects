import pandas

nato_list = pandas.read_csv("dayProjects/week3/NATOalphabet/natolist.csv")
nato_dict = {row["letter"]:row["word"] for (index, row) in nato_list.iterrows()}

word_input = input("Enter a word to translate with NATO: ").upper()
translate_list = [nato_dict[letter] for letter in word_input]
for i in range(len(word_input)):
    print(f"{word_input[i]} as in {translate_list[i]}.")
