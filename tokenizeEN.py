import nltk

InputFile = "/Users/yuanfeng/ComputerScience/AI/C-E datasetcopy/trainEN.txt"
OutputFile = "/Users/yuanfeng/ComputerScience/AI/C-E datasetcopy/trainEN_tokenized.txt"

lines = list(open(InputFile))

with open(OutputFile, "w") as f:
    f.write(
        "\n".join([
            " ".join(nltk.tokenize.word_tokenize(l))
            for l in lines
        ])
    )
